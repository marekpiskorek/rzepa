from rest_framework import viewsets

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
