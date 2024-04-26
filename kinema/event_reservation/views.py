from django.views.generic import CreateView, UpdateView, DeleteView
from .models import event_reservation
from .serializer import event_reservation_serializer
from rest_framework import generics, permissions, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import requests


class ERVCreateView(generics.CreateAPIView):
    queryset = event_reservation.objects.all()
    serializer_class = event_reservation_serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def upload_qrcode_to_cloudinary():
        counter = 0
        magic_word="event"+counter 
        QrCode_url = (
            "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={magic_word}"
        )
        response = requests.get(
            "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={magic_word}"
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


class ERVUpdateView(generics.UpdateAPIView):
    queryset = event_reservation.objects.all()
    serializer_class = event_reservation_serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class ERVDeleteView(generics.DestroyAPIView):
    queryset = event_reservation.objects.all()
    serializer_class = event_reservation_serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        ERV_id = request.data.get("id")
        ERV_event = request.data.get("movie")
        if ERV_id:
            try:
                theERV = event_reservation.objects.get(id=ERV_id)
                theERV.delete()
                return Response(
                    {"message": "ERV deleted successfully"},
                    status=status.HTTP_200_OK,
                )
            except event_reservation.DoesNotExist:
                return Response(
                    {"message": "ERV not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        elif ERV_event:
            try:
                theERV = event_reservation.objects.get(title=st_movie)
                theERV.delete()
                return Response(
                    {"message": "ERV deleted successfully"},
                    status=status.HTTP_200_OK,
                )
            except event_reservation.DoesNotExist:
                return Response(
                    {"message": "ERV not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            return Response(
                {"message": "Please provide either RV_id or RV_movie"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ERVDetailView(generics.RetrieveAPIView):
    queryset = event_reservation.objects.all()
    serializer_class = event_reservation_serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class E_ALL_RVS(generics.ListAPIView):
    queryset = event_reservation.objects.all()
    serializer_class = event_reservation_serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class ERVByMovieView(generics.ListAPIView):
    queryset = event_reservation.objects.all()

    serializer_class = event_reservation_serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        movie_id = self.kwargs.get("movie_id")
        return event_reservation.objects.filter(movie=movie_id)


class ERVByUSERView(generics.ListAPIView):
    queryset = event_reservation.objects.all()
    serializer_class = event_reservation_serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return event_reservation.objects.filter(User=user_id)
