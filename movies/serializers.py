from rest_framework import serializers
from .models import Movie, Genre

class GenreSerializer(serializers.ModelSerializer):
    """serializer for genre model"""
    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    """serializer for the movie model"""
    genre = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('name', 'imdb_score', 'popularity', 'director', 'genre')