from django.db import models


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="comments"
    )
    author = models.CharField(max_length=64, blank=True, default="Anonymous")
    text = models.TextField()
