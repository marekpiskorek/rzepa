from rest_framework import viewsets
from rest_framework.response import Response

from movies.models import Movie
from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def create(self, request):
        data = request.data.copy()
        movie_pk = data.pop("movie_id")
        try:
            movie = Movie.objects.get(id=movie_pk)
        except Movie.DoesNotExist:
            return Response({"string": "Movie with this id not found in the database"}, status=404)
        data["movie"] = movie
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(data, status=204)

    def list(self, request):
        if "movie_pk" in request.query_params:
            self.queryset = Comment.objects.filter(
                movie_id__in=request.query_params["movie_pk"]
            ).all()
        return super(CommentViewSet, self).list(request)
