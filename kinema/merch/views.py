from django.views.generic import CreateView, UpdateView, DeleteView
from .models import item
from .serializer import MerchSerializer
from rest_framework import generics, permissions, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class MerchCreateView(generics.CreateAPIView):
    queryset = item.objects.all()
    serializer_class = MerchSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class MerchUpdateView(generics.UpdateAPIView):
    queryset = item.objects.all()
    serializer_class = MerchSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class MerchDeleteView(generics.DestroyAPIView):
    queryset = item.objects.all()
    serializer_class = MerchSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        item_id = request.data.get("id")
        item_name = request.data.get("name")
        if item_id:
            try:
                theitem = item.objects.get(id=event_id)
                theitem.delete()
                return Response(
                    {"message": "item deleted successfully"},
                    status=status.HTTP_200_OK,
                )
            except item.DoesNotExist:
                return Response(
                    {"message": "item not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        elif item_name:
            try:
                theevent = event.objects.get(title=item_name)
                theevent.delete()
                return Response(
                    {"message": "item deleted successfully"},
                    status=status.HTTP_200_OK,
                )
            except item.DoesNotExist:
                return Response(
                    {"message": "item not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            return Response(
                {"message": "Please provide either merch_id or merch_name"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class MerchDetailView(generics.RetrieveAPIView):
    queryset = item.objects.all()
    serializer_class = MerchSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class AllMerch(generics.ListAPIView):
    queryset = item.objects.all()
    serializer_class = MerchSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]



class MerchByMovieView(generics.ListAPIView):
    serializer_class = MerchSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        movie_id = self.kwargs.get("movie_id")
        return item.objects.filter(movie=movie_id)