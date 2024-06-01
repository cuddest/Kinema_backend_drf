from django.shortcuts import render
from .models import User
from .serializer import UserSerializer
from rest_framework import generics, permissions, status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import JsonResponse
import jwt, datetime
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import authentication_classes, permission_classes
from django.db.models import Q
import random
import string
from django.core.mail import send_mail
from django.conf import settings


@authentication_classes([])
@permission_classes([])
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


@authentication_classes([])
@permission_classes([])
class LoginView(APIView):
    def post(self, request):

        email = request.data.get("email")
        password = request.data.get("password")
        username = request.data.get("username")
        user = User.objects.filter(Q(username=username) | Q(email=email)).first()

        if user is None:
            raise AuthenticationFailed("User not found!")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password!")

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        response = Response()
        response.set_cookie(key="jwt", value=access_token, httponly=True)
        response.set_cookie(key="refresh_token", value=str(refresh), httponly=True)
        response.data = {"jwt": access_token, "refresh_token": str(refresh)}

        return response


class UserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        username = request.data.get("username")
        user = User.objects.get(username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        username = request.data["username"]
        user = User.objects.get(username=username)
        user_id = user.id  # Get the user's ID

        response = Response()
        response.delete_cookie(key="jwt")
        response.data = {
            "message": "success",
            "user_id": user_id,
        }  # Include the user's ID in the response
        return response


class Fidelity_addU(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def post(self, request):

        try:
            username = request.data["username"]
            new_fidelity_points_change = request.data["fidelity_points_change"]
            user = User.objects.get(username=username)
            actual_fidelity_points = user.Fidelity_Points
            user.Fidelity_Points = actual_fidelity_points + new_fidelity_points_change
            user.save()
            return Response(
                {"message": "fidelity ponits updated"},
                status=status.HTTP_200_OK,
            )
        except user.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class user_update(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
