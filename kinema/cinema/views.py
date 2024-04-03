from django.views.generic import CreateView, UpdateView, DeleteView
from .models import cinema
from .serializer import cinemaSerializer
from rest_framework import generics, permissions, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# yes i called it cinema then mid the work realized it should be called hall because it is a hall not a cinema and a cinema has a lot of halls but fuck it im too fucking lazy to fix it
class cinemaCreateView(generics.CreateAPIView):
    queryset = cinema.objects.all()
    serializer_class = cinemaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class cinemaUpdateView(generics.UpdateAPIView):
    queryset = cinema.objects.all()
    serializer_class = cinemaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class cinemaDeleteView(generics.DestroyAPIView):
    queryset = cinema.objects.all()
    serializer_class = cinemaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        cinema_id = request.data.get("id")
        cinema_name = request.data.get("name")
        if cinema_id:
            try:
                thecinema = cinema.objects.get(id=cinema_id)
                thecinema.delete()
                return Response(
                    {"message": "cinema deleted successfully"},
                    status=status.HTTP_200_OK,
                )
            except cinema.DoesNotExist:
                return Response(
                    {"message": "cinema not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        elif cinema_name:
            try:
                theevent = cinema.objects.get(title=event_name)
                thecinema.delete()
                return Response(
                    {"message": "cinema deleted successfully"},
                    status=status.HTTP_200_OK,
                )
            except event.DoesNotExist:
                return Response(
                    {"message": "cinema not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            return Response(
                {"message": "Invalid request"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class cinemaListView(generics.ListAPIView):
    queryset = cinema.objects.all()
    serializer_class = cinemaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class cinemaDetailView(generics.RetrieveAPIView):
    queryset = cinema.objects.all()
    serializer_class = cinemaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
