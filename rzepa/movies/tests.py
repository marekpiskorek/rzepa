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
        Movie.objects.create(title="Gone With The Wind")
        Movie.objects.create(title="Godfather")
        Movie.objects.create(title="The Room")
        response = client.get("/movies/")
        assert response.status_code == 200
        assert sorted(response.data, key=lambda k: k["title"]) == [
            OrderedDict({"title": "Godfather"}),
            OrderedDict({"title": "Gone With The Wind"}),
            OrderedDict({"title": "The Room"}),
        ]
