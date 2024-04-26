from django.views.generic import CreateView, UpdateView, DeleteView
from .models import movie_reservation
from .serializer import Movie_Showtime_Serializer
from rest_framework import generics, permissions, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import requests


class RVCreateView(generics.CreateAPIView):
    queryset = Showtime.objects.all()
    serializer_class = Movie_Showtime_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def upload_qrcode_to_cloudinary():
        counter = 0
        QrCode_url = (
            "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={counter}"
        )
        response = requests.get(
            "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={counter}"
        )
        if response.status_code == 200:
            cloudinary_url = os.getenv("CLOUDINARY_URL")
            cloud_name = os.getenv("CLOUD_NAME")
            api_key = os.getenv("API_KEY_CLOUD")
            api_secret = os.getenv("API_SECRET")
            cloudinary.config(
                cloud_name=cloud_name, api_key=api_key, api_secret=api_secret
            )
            upload_result = cloudinary.uploader.upload(image_url)
            QrCode_url = upload_result.get("secure_url")
            counter += 1
            return QrCode_url

        else:
            print("Error generating QR code", response.status_code)
            return None

    def perform_create(self, serializer):
        instance = serializer.save()
        qr_code = upload_qrcode_to_cloudinary()
        if qr_code is not None:
            instance.qrcode = qr_code
            instance.save()


class RVUpdateView(generics.UpdateAPIView):
    queryset = movie_reservation.objects.all()
    serializer_class = Movie_Showtime_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class RVDeleteView(generics.DestroyAPIView):
    queryset = movie_reservation.objects.all()
    serializer_class = Movie_Showtime_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        RV_id = request.data.get("id")
        RV_movie = request.data.get("movie")
        if RV_id:
            try:
                theRV = movie_reservation.objects.get(id=st_id)
                theRV.delete()
                return Response(
                    {"message": "RV deleted successfully"},
                    status=status.HTTP_200_OK,
                )
            except movie_reservation.DoesNotExist:
                return Response(
                    {"message": "ST not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        elif RV_movie:
            try:
                thest = movie_reservation.objects.get(title=st_movie)
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
    serializer_class = Movie_Showtime_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class ALL_RVS(generics.ListAPIView):
    queryset = movie_reservation.objects.all()
    serializer_class = Movie_Showtime_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class RVByMovieView(generics.ListAPIView):
    queryset = movie_reservation.objects.all()

    serializer_class = Movie_Showtime_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        movie_id = self.kwargs.get("movie_id")
        return movie_reservation.objects.filter(movie=movie_id)


class RVByUSERView(generics.ListAPIView):
    queryset = movie_reservation.objects.all()
    serializer_class = Movie_Showtime_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return movie_reservation.objects.filter(User=user_id)
