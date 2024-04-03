from django.views.generic import CreateView, UpdateView, DeleteView
from .models import review
from .serializer import ReviewSerializer
from rest_framework import generics, permissions, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ReviewCreateView(generics.CreateAPIView):
    queryset = review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class RewiewUpdateView(generics.UpdateAPIView):
    queryset = review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class RewiewDeleteView(generics.DestroyAPIView):
    queryset = review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        review_id = request.data.get("id")
        if review_id:
            try:
                theReview = review.objects.get(id=review_id)
                theReview.delete()
                return Response(
                    {"message": "Review deleted successfully"},
                    status=status.HTTP_200_OK,
                )
            except cinema.DoesNotExist:
                return Response(
                    {"message": "Rewiew not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            return Response(
                {"message": "Invalid request"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ReviewListView(generics.ListAPIView):
    queryset = review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class ReviewDetailView(generics.RetrieveAPIView):
    queryset = review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class ReviewsByMovieView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        movie_id = self.kwargs.get("movie_id")
        return review.objects.filter(movie=movie_id)


class ReviewsByUserView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return review.objects.filter(user=user_id)



