from django.db.models import Count

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from movies.api_clients import OMDbAPIClient
from movies.models import Movie
from movies.serializers import MovieSerializer, RatingSerializer


class MovieViewSet(ModelViewSet):
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


class TopMoviesView(APIView):
    def get(self, request, format=None):
        date_from = request.query_params.get("from")
        date_to = request.query_params.get("to")
        qs = Movie.objects.prefetch_related("comments").annotate(
            total_comments=Count("comments")
        )
        if date_from:
            qs = qs.filter(comments__created_at__gte=date_from)
        if date_to:
            qs = qs.filter(comments__created_at__lte=date_to)
        qs = qs.values("id", "total_comments").order_by("-total_comments")
        response = []
        last_count = 0
        last_rank = 0
        for element in qs.all():
            if not last_rank or element["total_comments"] < last_count:
                last_rank += 1
            last_count = element["total_comments"]
            element["rank"] = last_rank
            element["movie_id"] = element.pop("id")  # rename the key
            response.append(element)
        return Response(response, status=200)
