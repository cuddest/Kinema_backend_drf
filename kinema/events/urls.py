from django.urls import path
from .views import (
    EventCreateView,
    EventDetailView,
    EventUpdateView,
    EventDeleteView,
    AllEvents,
)

urlpatterns = [
    path("add", EventCreateView.as_view()),
    path("update/<int:pk>", EventUpdateView.as_view()),
    path("delete/<int:pk>", EventDeleteView.as_view()),
    path("details/<int:pk>", EventDetailView.as_view()),
    path("list", AllEvents.as_view()),
]
