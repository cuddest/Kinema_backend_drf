from django.urls import path
from .views import (
    RVCreateView,
    RVUpdateView,
    RVDeleteView,
    RVDetailView,
    ALL_RVS,
    RVByMovieView,
    RVByUSERView,
)


urlpatterns = [
    path("add", RVCreateView.as_view()),
    path("update/<int:pk>", RVUpdateView.as_view()),
    path("delete/<int:pk>", RVDeleteView.as_view()),
    path("details/<int:pk>", RVDetailView.as_view()),
    path("list", ALL_RVS.as_view()),
    path("movie/<int:movie_id>", RVByMovieView.as_view()),
    path("theatre/<int:theatre_id>", RVByUSERView.as_view()),
]
