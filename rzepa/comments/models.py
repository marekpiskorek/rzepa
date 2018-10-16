from datetime import datetime, timezone

from django.db import models


class Comment(models.Model):
    created_at = models.DateTimeField(blank=True, default=datetime.now(tz=timezone.utc))
    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="comments"
    )
    author = models.CharField(max_length=64, blank=True, default="Anonymous")
    text = models.TextField()
