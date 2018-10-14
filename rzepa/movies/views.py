from rest_framework import viewsets
from rest_framework.response import Response

from movies.api_clients import OMDbAPIClient
from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def create(self, request):
        try:
            title = request.data["title"]
        except KeyError:
            return Response(status=400)
        data = OMDbAPIClient().fetch(title)
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(data, status=201)
