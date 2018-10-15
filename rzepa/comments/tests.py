import pytest

from comments.models import Comment
from movies.models import Movie


@pytest.mark.django_db
class TestCommentsEndpoint:
    def test_get_all_comments_from_empty_table(self, client):
        response = client.get("/comments/")
        assert response.status_code == 200
        assert response.data == []

    def test_get_all_comments(self, client):
        movie = Movie.objects.create(title="Godfather")
        Comment.objects.create(movie=movie, text="Positive comment")
        response = client.get("/comments/")
        assert response.status_code == 200
        returned_comment, = response.data
        assert returned_comment["movie"] == "Godfather"
        assert returned_comment["text"] == "Positive comment"
        assert returned_comment["author"] == "Anonymous"

    def test_return_comments_for_given_movie(self, client):
        movie = Movie.objects.create(title="Godfather")
        another_movie = Movie.objects.create(title="The Room")
        Comment.objects.create(movie=movie, text="Positive comment")
        Comment.objects.create(movie=another_movie, text="Negative comment")
        response = client.get("/comments/", {"movie_pk": movie.id})
        assert response.status_code == 200
        assert len(response.data) == 1
        returned_comment, = response.data
        assert returned_comment["text"] == "Positive comment"
