from rest_framework import viewsets

from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewset):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
