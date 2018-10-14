import pytest

from movies.models import Movie


@pytest.mark.django_db
class TestMoviesEndpoint:
    def test_get_on_empty_database_returns_empty_list(self, client):
        response = client.get("/movies/")
        assert response.status_code == 200
        assert response.data == []

    def test_get_all_exsisting_movies(self, client):
        movie_1 = Movie.objects.create(title="Godfather")
        movie_2 = Movie.objects.create(title="Gone With The Wind")
        movie_3 = Movie.objects.create(title="The Room")
        response = client.get("/movies/")
        assert response.status_code == 200
        response_movie_1, response_movie_2, response_movie_3 = sorted(
            response.data, key=lambda k: k["Title"]
        )
        assert response_movie_1["Title"] == movie_1.title
        assert response_movie_2["Title"] == movie_2.title
        assert response_movie_3["Title"] == movie_3.title

    def test_post_without_title_fails(self, client):
        response = client.post("/movies/", {})
        assert response.status_code == 400

    def test_post_with_title_returns_created_movie_data(self, client):
        response = client.post("/movies/", {"title": "Citizen Kane"})
        assert response.status_code == 201
        assert response.data["Title"] == "Citizen Kane"
