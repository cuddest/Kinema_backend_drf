from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Notification
from .serializer import NotificationSerializer
from rest_framework import generics, permissions, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import requests


class NotifCreate(generics.CreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class NotifUpdate(generics.UpdateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class NotifDelete(generics.DestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        NF_id = request.data.get("id")
        NF_User = request.data.get("User")
        if NF_id:
            try:
                theNF = Notification.objects.get(id=NF_id)
                theNf.delete()
                return Response(
                    {"message": "NF deleted successfully"},
                    status=status.HTTP_200_OK,
                )
            except Notification.DoesNotExist:
                return Response(
                    {"message": "NF not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        elif NF_User:
            try:
                theNF = Notification.objects.get(title=NF_movie)
                theNF.delete()
                return Response(
                    {"message": "NF deleted successfully"},
                    status=status.HTTP_200_OK,
                )
            except Notification.DoesNotExist:
                return Response(
                    {"message": "NF not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            return Response(
                {"message": "Please provide either NF_id or NF_User"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class NFDetailView(generics.RetrieveAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class ALL_NFS(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class NFByMovieView(generics.ListAPIView):
    queryset = Notification.objects.all()

    serializer_class = NotificationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        movie_id = self.kwargs.get("User_id")
        return Notification.objects.filter(movie=User_id)
