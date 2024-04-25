from django.urls import path
from .views import (
    STEByMovieView,
    STECreateView,
    STEDeleteView,
    STEUpdateView,
    ALL_SHOW_TIMES_EVENTS,
    STEDetailView,
    STEByMovieView,
    STEByTheatreView,
)


urlpatterns = [
    path("add", STECreateView.as_view()),
    path("update/<int:pk>", STEUpdateView.as_view()),
    path("delete/<int:pk>", STEDeleteView.as_view()),
    path("details/<int:pk>", STEDetailView.as_view()),
    path("list", ALL_SHOW_TIMES_EVENTS.as_view()),
    path("movie/<int:movie_id>", STEByMovieView.as_view()),
    path("theatre/<int:theatre_id>", STEByTheatreView.as_view()),
]
