from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Showtime
from .serializer import Movie_Showtime_Serializer
from rest_framework import generics, permissions, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class STCreateView(generics.CreateAPIView):
    queryset = Showtime.objects.all()
    serializer_class = Movie_Showtime_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class STUpdateView(generics.UpdateAPIView):
    queryset = Showtime.objects.all()
    serializer_class = Movie_Showtime_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class STDeleteView(generics.DestroyAPIView):
    queryset = Showtime.objects.all()
    serializer_class = Movie_Showtime_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        st_id = request.data.get("id")
        st_movie = request.data.get("movie")
        if st_id:
            try:
                thest = Showtime.objects.get(id=st_id)
                thest.delete()
                return Response(
                    {"message": "ST deleted successfully"},
                    status=status.HTTP_200_OK,
                )
            except Showtime.DoesNotExist:
                return Response(
                    {"message": "ST not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        elif st_movie:
            try:
                thest = Showtime.objects.get(title=st_movie)
                thest.delete()
                return Response(
                    {"message": "ST deleted successfully"},
                    status=status.HTTP_200_OK,
                )
            except Showtime.DoesNotExist:
                return Response(
                    {"message": "ST not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            return Response(
                {"message": "Please provide either st_id or st_movie"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class STDetailView(generics.RetrieveAPIView):
    queryset = Showtime.objects.all()
    serializer_class = Movie_Showtime_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class ALL_SHOW_TIMES(generics.ListAPIView):
    queryset = Showtime.objects.all()
    serializer_class = Movie_Showtime_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class STByMovieView(generics.ListAPIView):
    serializer_class = class MerchByMovieView(generics.ListAPIView):
    serializer_class = MerchSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        movie_id = self.kwargs.get("movie_id")
        return item.objects.filter(movie=movie_id)

class STByTheatreView(generics.ListAPIView):
    serializer_class = class MerchByMovieView(generics.ListAPIView):
    serializer_class = MerchSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        theatre_id = self.kwargs.get("theatre_id")
        return item.objects.filter(theatre=theatre_id)