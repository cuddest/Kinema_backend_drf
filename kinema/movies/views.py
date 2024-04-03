import requests
from .models import Movie
import json
import os
from dotenv import load_dotenv
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import MovieSerializer
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv
import os
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.pagination import PageNumberPagination
from rest_framework.status import (
    HTTP_404_NOT_FOUND,
    HTTP_201_CREATED,
    HTTP_401_UNAUTHORIZED,
    HTTP_400_BAD_REQUEST,
)


def upload_image_to_cloudinary(movie_id):
    api_key = os.getenv("API_KEY_TMDB")
    base_url3 = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    endpoint3 = f"{base_url3}?api_key={api_key}"
    response3 = requests.get(endpoint3)
    data3 = response3.json()
    image_path = data3["posters"][0]["file_path"]
    image_url = f"https://image.tmdb.org/t/p/original{image_path}"
    load_dotenv()
    cloudinary_url = os.getenv("CLOUDINARY_URL")
    cloud_name = os.getenv("CLOUD_NAME")
    api_key = os.getenv("API_KEY_CLOUD")
    api_secret = os.getenv("API_SECRET")
    cloudinary.config(cloud_name=cloud_name, api_key=api_key, api_secret=api_secret)
    upload_result = cloudinary.uploader.upload(image_url)
    photo_url = upload_result.get("secure_url")
    return photo_url


def get_movie_info(movie_id):
    api_key = os.getenv("API_KEY_TMDB")
    base_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    endpoint = f"{base_url}?api_key={api_key}"
    endpoint2 = f"{base_url}/credits?api_key={api_key}"
    response = requests.get(endpoint)
    response2 = requests.get(endpoint2)
    data = response.json()
    data2 = response2.json()
    if response.status_code == 404:
        data = {"message": "The movie ID does not exist"}
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    movie = Movie()
    title = data.get("title")
    print(title)
    movie.title = title
    movie.Movie_Cast = [cast["name"] for cast in data2["cast"]]
    movie.Description = data["overview"]
    movie.Release_Date = data["release_date"]
    movie.Genre = [genre["name"] for genre in data["genres"]]
    movie.Category = "Adult" if data["adult"] else "Family"
    movie.Language = data["original_language"]
    movie.Duration = data["runtime"]
    movie.ProductionCompanies = [
        production_companies["name"]
        for production_companies in data["production_companies"]
    ]
    movie.country = [
        production_countries["name"]
        for production_countries in data["production_countries"]
    ]
    movie.release_date = data["release_date"]
    poster_link = upload_image_to_cloudinary(movie_id)
    print("haha", poster_link)
    movie.Poster = poster_link
    movie.save()
    return movie


class add_movie(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Check for JWT token authenticity (assuming JWTAuthentication raises AuthenticationFailed)
            user = JWTAuthentication().authenticate(request)  # Authenticate using JWT
            movie_id = request.data.get("movie_id")
            movie = get_movie_info(movie_id)
            if not isinstance(movie, Movie):
                return Response(
                    "Movie with this ID not found in the TMDB DB",
                    status=HTTP_404_NOT_FOUND,
                )

            else:
                movie.save()
                return Response("created !!", status=HTTP_201_CREATED)
        except AuthenticationFailed:
            return Response("Authentication failed", status=HTTP_401_UNAUTHORIZED)


class delete_movie(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def delete(self, request, *args, **kwargs):
        movie_id = request.data.get("movie_id")
        movie_name = request.data.get("movie_name")

        if movie_id:
            try:
                movie = Movie.objects.get(id=movie_id)
                movie.delete()
                return Response(
                    {"message": "Movie deleted successfully"},
                    status=status.HTTP_200_OK,
                )
            except Movie.DoesNotExist:
                return Response(
                    {"message": "Movie not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        elif movie_name:
            try:
                movie = Movie.objects.get(title=movie_name)
                movie.delete()
                return Response(
                    {"message": "Movie deleted successfully"},
                    status=status.HTTP_200_OK,
                )
            except Movie.DoesNotExist:
                return Response(
                    {"message": "Movie not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            return Response(
                {"message": "Please provide either movie_id or movie_name"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class display_movies(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class PaginatedMovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class.page_size = 10
    pagination_class.page_size_query_param = "page_size"
    pagination_class.max_page_size = 100
