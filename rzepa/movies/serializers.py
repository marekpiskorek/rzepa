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
        )

    Title = serializers.CharField(source="title")
    Year = serializers.CharField(source="year")
    Rated = serializers.CharField(source="rated")
    Released = serializers.CharField(source="released")
    Runtime = serializers.CharField(source="runtime")
    Genre = serializers.CharField(source="genre")
    Director = serializers.CharField(source="director")
    Writer = serializers.CharField(source="writer")
    Actors = serializers.CharField(source="actors")
    Plot = serializers.CharField(source="plot")
    Language = serializers.CharField(source="language")
    Country = serializers.CharField(source="country")
    Awards = serializers.CharField(source="awards")
    Poster = serializers.CharField(source="poster")
    Ratings = RatingSerializer(many=True, read_only=True)
    Metascore = serializers.CharField(source="metascore")
    Type = serializers.CharField(source="type")
    DVD = serializers.CharField(source="dvd")
    BoxOffice = serializers.CharField(source="box_office")
    Production = serializers.CharField(source="production")
    Website = serializers.CharField(source="website")
