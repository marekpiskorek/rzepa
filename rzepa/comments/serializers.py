from rest_framework import serializers

from comments.models import Comment
from movies.models import Movie
from movies.serializers import ReferencedMovieSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("movie", "text", "author")

    movie = ReferencedMovieSerializer()


class CommentPostSerializer(CommentSerializer):
    class Meta:
        model = Comment
        fields = ("movie", "text", "author")

    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
