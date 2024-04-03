from django.urls import path
from .views import (
    MerchCreateView,
    MerchUpdateView,
    MerchDeleteView,
    MerchDetailView,
    MerchByMovieView,
    AllMerch,
)


urlpatterns = [
    path("add", MerchCreateView.as_view()),
    path("update/<int:pk>", MerchUpdateView.as_view()),
    path("delete/<int:pk>", MerchDeleteView.as_view()),
    path("details/<int:pk>", MerchDetailView.as_view()),
    path("movie/<int:movie_id>", MerchByMovieView.as_view()),
    path("list", AllMerch.as_view()),
]
