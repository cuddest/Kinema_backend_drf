from django.urls import path
from .views import (
    cinemaListView,
    cinemaCreateView,
    cinemaDetailView,
    cinemaUpdateView,
    cinemaDeleteView,
)

urlpatterns = [
    path("list/", cinemaListView.as_view(), name="list"),
    path("create/", cinemaCreateView.as_view(), name="create"),
    path("detail/<int:pk>/", cinemaDetailView.as_view(), name="detail"),
    path("update/<int:pk>/", cinemaUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", cinemaDeleteView.as_view(), name="delete"),
]
 
