from rest_framework import viewsets

from comments.models import Comment
from comments.serializers import CommentSerializer, CommentPostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_serializer_class(self):
        return (
            CommentPostSerializer
            if self.request.method == "POST"
            else CommentSerializer
        )

    def get_queryset(self):
        if "movie_pk" in self.request.query_params:
            return Comment.objects.filter(
                movie_id__in=self.request.query_params.get("movie_pk")
            ).all()
        else:
            return Comment.objects.all()
