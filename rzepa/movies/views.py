from rest_framework import viewsets
from rest_framework.response import Response

from movies.api_clients import OMDbAPIClient
from movies.models import Movie
from movies.serializers import MovieSerializer, RatingSerializer


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def create(self, request):
        try:
            title = request.data["title"]
        except KeyError:
            return Response(status=400)
        data = OMDbAPIClient().fetch(title)
        ratings = data.pop("Ratings", [])
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            movie = serializer.save()
            for rating in ratings:
                rating["movie_id"] = movie.id
                rating_serializer = RatingSerializer(data=rating)
                if rating_serializer.is_valid():
                    rating_serializer.save()
        data["Ratings"] = ratings
        return Response(data, status=201)
