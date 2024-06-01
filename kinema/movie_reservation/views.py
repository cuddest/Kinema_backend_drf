from django.views.generic import CreateView, UpdateView, DeleteView
from .models import movie_reservation
from movie_showtime.models import Showtime
from .serializer import movie_reservation_Serializer
from rest_framework import generics, permissions, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import requests


class RVCreateView(generics.CreateAPIView):
    queryset = movie_reservation.objects.all()
    serializer_class = movie_reservation_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class RVUpdateView(generics.UpdateAPIView):
    queryset = movie_reservation.objects.all()
    serializer_class = movie_reservation_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class RVDeleteView(generics.DestroyAPIView):
    queryset = movie_reservation.objects.all()
    serializer_class = movie_reservation_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        RV_id = request.data.get("id")
        RV_movie = request.data.get("movie")
        if RV_id:
            try:
                theRV = movie_reservation.objects.get(id=RV_id)
                theRV.delete()
                return Response(
                    {"message": "RV deleted successfully"},
                    status=status.HTTP_200_OK,
                )
            except movie_reservation.DoesNotExist:
                return Response(
                    {"message": "RV not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        elif RV_movie:
            try:
                thest = movie_reservation.objects.get(title=RV_movie)
                thest.delete()
                return Response(
                    {"message": "RV deleted successfully"},
                    status=status.HTTP_200_OK,
                )
            except movie_reservation.DoesNotExist:
                return Response(
                    {"message": "RV not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            return Response(
                {"message": "Please provide either RV_id or RV_movie"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class RVDetailView(generics.RetrieveAPIView):
    queryset = movie_reservation.objects.all()
    serializer_class = movie_reservation_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class ALL_RVS(generics.ListAPIView):
    queryset = movie_reservation.objects.all()
    serializer_class = movie_reservation_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        reservations = movie_reservation.objects.all()
        for reservation in reservations:
            showtime_id = reservation.showtime_id
            showtime = Showtime.objects.get(id=showtime_id)
            reservation.showtime = showtime
        return reservations


class RVByMovieView(generics.ListAPIView):
    queryset = movie_reservation.objects.all()

    serializer_class = movie_reservation_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        movie_id = self.kwargs.get("movie_id")
        return movie_reservation.objects.filter(movie=movie_id)


class RVByUSERView(generics.ListAPIView):
    queryset = movie_reservation.objects.all()
    serializer_class = movie_reservation_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return movie_reservation.objects.filter(User=user_id)
