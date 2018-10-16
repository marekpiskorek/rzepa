from rest_framework import serializers

from movies.models import Movie, Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ("Source", "Value", "movie")

    Source = serializers.CharField(source="source")
    Value = serializers.CharField(source="value")


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            "Title",
            "Year",
            "Rated",
            "Released",
            "Runtime",
            "Genre",
            "Director",
            "Writer",
            "Actors",
            "Plot",
            "Language",
            "Country",
            "Awards",
            "Poster",
            "Ratings",
            "Metascore",
            "imdbRating",
            "imdbVotes",
            "imdbID",
            "Type",
            "DVD",
            "BoxOffice",
            "Production",
            "Website",
            "id",
        )

    Title = serializers.CharField(source="title")
    Year = serializers.CharField(source="year", required=False)
    Rated = serializers.CharField(source="rated", required=False)
    Released = serializers.CharField(source="released", required=False)
    Runtime = serializers.CharField(source="runtime", required=False)
    Genre = serializers.CharField(source="genre", required=False)
    Director = serializers.CharField(source="director", required=False)
    Writer = serializers.CharField(source="writer", required=False)
    Actors = serializers.CharField(source="actors", required=False)
    Plot = serializers.CharField(source="plot", required=False)
    Language = serializers.CharField(source="language", required=False)
    Country = serializers.CharField(source="country", required=False)
    Awards = serializers.CharField(source="awards", required=False)
    Poster = serializers.CharField(source="poster", required=False)
    Ratings = RatingSerializer(many=True, read_only=True, required=False)
    Metascore = serializers.CharField(source="metascore", required=False)
    Type = serializers.CharField(source="type", required=False)
    DVD = serializers.CharField(source="dvd", required=False)
    BoxOffice = serializers.CharField(source="box_office", required=False)
    Production = serializers.CharField(source="production", required=False)
    Website = serializers.CharField(source="website", required=False)


class ReferencedMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("title",)
