from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Showtime_events
from .serializer import Event_Showtime_Serializer
from rest_framework import generics, permissions, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class STECreateView(generics.CreateAPIView):
    queryset = Showtime_events.objects.all()
    serializer_class = Event_Showtime_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class STEUpdateView(generics.UpdateAPIView):
    queryset = Showtime_events.objects.all()
    serializer_class = Event_Showtime_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class STEDeleteView(generics.DestroyAPIView):
    queryset = Showtime_events.objects.all()
    serializer_class = Event_Showtime_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        ste_id = request.data.get("id")
        ste = request.data.get("movie")
        if ste_id:
            try:
                theste = Showtime_events.objects.get(id=st_id)
                theste.delete()
                return Response(
                    {"message": "STE deleted successfully"},
                    status=status.HTTP_200_OK,
                )
            except Showtime_events.DoesNotExist:
                return Response(
                    {"message": "STe not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        elif ste:
            try:
                thest = Showtime_events.objects.get(title=st_movie)
                thest.delete()
                return Response(
                    {"message": "STe deleted successfully"},
                    status=status.HTTP_200_OK,
                )
            except Showtime_events.DoesNotExist:
                return Response(
                    {"message": "STe not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            return Response(
                {"message": "Please provide either ste_id or st_movie"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class STEDetailView(generics.RetrieveAPIView):
    queryset = Showtime_events.objects.all()
    serializer_class = Event_Showtime_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class ALL_SHOW_TIMES_EVENTS(generics.ListAPIView):
    queryset = Showtime_events.objects.all()
    serializer_class = Event_Showtime_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class STEByMovieView(generics.ListAPIView):
    queryset = Showtime_events.objects.all()
    serializer_class = Event_Showtime_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        movie_id = self.kwargs.get("movie_id")
        return item.objects.filter(movie=movie_id)


class STEByTheatreView(generics.ListAPIView):
    queryset = Showtime_events.objects.all()
    serializer_class = Event_Showtime_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        theatre_id = self.kwargs.get("theatre_id")
        return item.objects.filter(theatre=theatre_id)
