from rest_framework import serializers

from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("movie", "text", "author")

    movie = serializers.PrimaryKeyRelatedField(read_only=True)