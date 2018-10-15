import pytest

from comments.models import Comment
from movies.api_clients import OMDbAPIClient
from movies.fixtures import movie_citizen_kane
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

    def test_post_with_title_returns_created_movie_data(self, client, mocker):
        mocker.patch.object(OMDbAPIClient, "fetch", return_value=movie_citizen_kane())
        response = client.post("/movies/", {"title": "Citizen Kane"})
        assert response.status_code == 201
        assert response.data["Title"] == "Citizen Kane"
        assert response.data["Production"] == "RKO Radio Pictures"

    def test_ratings_are_created_with_movies(self, client, mocker):
        mocker.patch.object(OMDbAPIClient, "fetch", return_value=movie_citizen_kane())
        response = client.post("/movies/", {"title": "Citizen Kane"})
        assert response.status_code == 201
        assert response.data["Title"] == "Citizen Kane"
        ratings = sorted(response.data["Ratings"], key=lambda k: k["Source"])
        assert ratings[0]["Source"] == "Internet Movie Database"
        assert ratings[0]["Value"] == "8.4/10"
        assert ratings[1]["Source"] == "Metacritic"
        assert ratings[1]["Value"] == "100/100"
        assert ratings[2]["Source"] == "Rotten Tomatoes"
        assert ratings[2]["Value"] == "100%"


@pytest.mark.django_db
class TestTopMoviesEndpoint:
    def test_endpoint_on_empty_db(self, client):
        response = client.get("/top/")
        assert response.status_code == 200
        assert response.data == []

    def test_single_movie_no_comments_is_returned(self, client):
        movie = Movie.objects.create(title="Godfather")
        response = client.get("/top/")
        assert response.status_code == 200
        assert response.data == [{"movie_id": movie.id, "rank": 1, "total_comments": 0}]

    def test_movie_with_comments_get_comments_counted_correctly(self, client):
        movie = Movie.objects.create(title="Godfather")
        Comment.objects.create(movie=movie, text="It was ok")
        Comment.objects.create(movie=movie, text="I fell asleep after half an hour")
        Comment.objects.create(movie=movie, text="I think Marlon Brando was hot")
        response = client.get("/top/")
        assert response.status_code == 200
        assert response.data == [{"movie_id": movie.id, "rank": 1, "total_comments": 3}]

    def test_more_than_one_movie_with_comments(self, client):
        movie_1 = Movie.objects.create(title="Godfather")
        Comment.objects.create(movie=movie_1, text="It was ok")
        Comment.objects.create(movie=movie_1, text="I fell asleep after half an hour")
        Comment.objects.create(movie=movie_1, text="I think Marlon Brando was hot")
        movie_2 = Movie.objects.create(title="The Room")
        Comment.objects.create(
            movie=movie_2, text="Masterpiece beyond our understanding"
        )
        Comment.objects.create(movie=movie_2, text="New look at modern drama")
        movie_3 = Movie.objects.create(title="Fantastic Four")
        response = client.get("/top/")
        assert response.status_code == 200
        assert response.data == [
            {"movie_id": movie_1.id, "rank": 1, "total_comments": 3},
            {"movie_id": movie_2.id, "rank": 2, "total_comments": 2},
            {"movie_id": movie_3.id, "rank": 3, "total_comments": 0},
        ]

    def test_tie_in_comment_number_results_in_the_same_rank(self, client):
        movie_1 = Movie.objects.create(title="Godfather")
        Comment.objects.create(movie=movie_1, text="It was ok")
        movie_2 = Movie.objects.create(title="The Room")
        Comment.objects.create(
            movie=movie_2, text="Masterpiece beyond our understanding"
        )
        movie_3 = Movie.objects.create(title="Fantastic Four")
        response = client.get("/top/")
        assert response.status_code == 200
        assert response.data == [
            {"movie_id": movie_1.id, "rank": 1, "total_comments": 1},
            {"movie_id": movie_2.id, "rank": 1, "total_comments": 1},
            {"movie_id": movie_3.id, "rank": 2, "total_comments": 0},
        ]
