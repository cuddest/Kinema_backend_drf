"""kinema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("movies/", include("movies.urls")),
    path("cinephile/", include("cinephile.urls")),
    path("events/", include("events.urls")),
    path("review/", include("review.urls")),
    path("cinema/", include("cinema.urls")),
    path("merch/", include("merch.urls")),
    path("event_showtime/", include("event_showtime.urls")),
    path("movie_showtime/", include("movie_showtime.urls")),
    path("movie_reservation/", include("movie_reservation.urls")),
    path("event_reservation/", include("event_reservation.urls")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
