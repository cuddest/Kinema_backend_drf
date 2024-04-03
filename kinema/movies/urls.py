from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("list/", views.display_movies.as_view(), name="register"),
    path("add/", views.add_movie.as_view(), name="add_movie"),
    path("delete/", views.delete_movie.as_view(), name="delete_movie"),
    path("details/<int:pk>", views.MovieDetailView.as_view(), name="details_movie"),
    path("paginated/", views.PaginatedMovieListView.as_view(), name="paginated_movie"),
]
