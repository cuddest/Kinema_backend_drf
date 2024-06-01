from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    UserView,
    LogoutView,
    Fidelity_addU,
    user_update,
)

urlpatterns = [
    path("register", RegisterView.as_view()),
    path("update/<int:pk>", user_update.as_view()),
    path("login", LoginView.as_view()),
    path("user", UserView.as_view()),
    path("logout", LogoutView.as_view()),
    path("Fidelity", Fidelity_addU.as_view()),
]
