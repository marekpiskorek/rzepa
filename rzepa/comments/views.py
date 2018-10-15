from rest_framework import viewsets
from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def create(self, request):
        breakpoint()
        return super(CommentViewSet, self).create(request)

    def list(self, request):
        if "movie_pk" in request.query_params:
            self.queryset = Comment.objects.filter(
                movie_id__in=request.query_params["movie_pk"]
            ).all()
        return super(CommentViewSet, self).list(request)
