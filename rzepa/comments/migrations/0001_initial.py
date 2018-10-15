# Generated by Django 2.1.2 on 2018-10-14 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [("movies", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "author",
                    models.CharField(blank=True, default="Anonymous", max_length=64),
                ),
                ("text", models.TextField()),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="movies.Movie",
                    ),
                ),
            ],
        )
    ]