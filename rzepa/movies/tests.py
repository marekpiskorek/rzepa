from collections import OrderedDict

import pytest

from movies.models import Movie


class TestMoviesEndpoint:
    @pytest.mark.django_db
    def test_get_on_empty_database_returns_empty_list(self, client):
        response = client.get("/movies/")
        assert response.status_code == 200
        assert response.data == []

    @pytest.mark.django_db
    def test_get_all_exsisting_movies(self, client):
        movie_1 = Movie.objects.create(title="Godfather")
        movie_2 = Movie.objects.create(title="Gone With The Wind")
        movie_3 = Movie.objects.create(title="The Room")
        response = client.get("/movies/")
        assert response.status_code == 200
        response_movie_1, response_movie_2, response_movie_3 = sorted(
            response.data, key=lambda k: k["title"]
        )
        assert response_movie_1["title"] == movie_1.title
        assert response_movie_2["title"] == movie_2.title
        assert response_movie_3["title"] == movie_3.title

    @pytest.mark.django_db
    def test_post_without_title_fails(self, client):
        response = client.post("/movies/", {})
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_post_with_title_returns_created_movie_data(self, client):
        response = client.post("/movies/", {"title": "Citizen Kane"})
        assert response.status_code == 201
        assert response.data["title"] == "Citizen Kane"
