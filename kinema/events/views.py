from django.views.generic import CreateView, UpdateView, DeleteView
from .models import event
from .serializer import EventSerializer
from rest_framework import generics, permissions, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class EventCreateView(generics.CreateAPIView):
    queryset = event.objects.all()
    serializer_class = EventSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class EventUpdateView(generics.UpdateAPIView):
    queryset = event.objects.all()
    serializer_class = EventSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class EventDeleteView(generics.DestroyAPIView):
    queryset = event.objects.all()
    serializer_class = EventSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        event_id = request.data.get("id")
        event_name = request.data.get("name")
        if event_id:
            try:
                theevent = event.objects.get(id=event_id)
                theevent.delete()
                return Response(
                    {"message": "event deleted successfully"},
                    status=status.HTTP_200_OK,
                )
            except event.DoesNotExist:
                return Response(
                    {"message": "event not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        elif event_name:
            try:
                theevent = event.objects.get(title=event_name)
                theevent.delete()
                return Response(
                    {"message": "event deleted successfully"},
                    status=status.HTTP_200_OK,
                )
            except event.DoesNotExist:
                return Response(
                    {"message": "event not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            return Response(
                {"message": "Please provide either event_id or event_name"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class EventDetailView(generics.RetrieveAPIView):
    queryset = event.objects.all()
    serializer_class = EventSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class AllEvents(generics.ListAPIView):
    queryset = event.objects.all()
    serializer_class = EventSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
