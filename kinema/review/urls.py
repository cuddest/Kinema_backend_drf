from django.urls import path
from .views import (
    ReviewCreateView,
    RewiewUpdateView,
    RewiewDeleteView,
    ReviewDetailView,
    ReviewsByMovieView,
    ReviewsByUserView,
    ReviewListView,
)

urlpatterns = [
    path("add", ReviewCreateView.as_view()),
    path("update/<int:pk>", RewiewUpdateView.as_view()),
    path("delete/<int:pk>", RewiewDeleteView.as_view()),
    path("details/<int:pk>", ReviewDetailView.as_view()),
    path("movie/<int:movie_id>", ReviewsByMovieView.as_view()),
    path("user/<int:user_id>", ReviewsByUserView.as_view()),
    path("list", ReviewListView.as_view()),
]
