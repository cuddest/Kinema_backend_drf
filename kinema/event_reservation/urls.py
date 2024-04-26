from django.urls import path
from .views import (
    ERVCreateView,
    ERVUpdateView,
    ERVDeleteView,
    ERVDetailView,
    E_ALL_RVS,
    ERVByMovieView,
    ERVByUSERView,
)


urlpatterns = [
    path("add", ERVCreateView.as_view()),
    path("update/<int:pk>", ERVUpdateView.as_view()),
    path("delete/<int:pk>", ERVDeleteView.as_view()),
    path("details/<int:pk>", ERVDetailView.as_view()),
    path("list", E_ALL_RVS.as_view()),
    path("movie/<int:movie_id>", ERVByMovieView.as_view()),
    path("theatre/<int:theatre_id>", ERVByUSERView.as_view()),
]
