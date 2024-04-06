from django.urls import path
from .views import (
  STByMovieView
  STCreateView,
  STDeleteView,
    STUpdateView,
    AllST,
    STDetailView,
    STByMovieView,
    STByTheatreView,
)


urlpatterns = [
    path("add", STCreateView.as_view()),
    path("update/<int:pk>", STUpdateView.as_view()),
    path("delete/<int:pk>", STDeleteView.as_view()),
    path("details/<int:pk>", STDetailView.as_view()),
    path("list", AllST.as_view()),
    path("movie/<int:movie_id>", STByMovieView.as_view()),
    path("theatre/<int:theatre_id>", STByTheatreView.as_view()),
]
