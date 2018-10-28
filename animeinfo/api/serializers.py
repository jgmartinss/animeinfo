from rest_framework import serializers

from animeinfo.core import models


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ('name', 'date_of_birth', 'nationality', 'about_of',)



class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genres
        fields = ('name',)



class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Episode
        fields = (
            'title', 'original_title',
            'type_ep', 'number_episode',
            'release_date_of'
        )


class AnimeSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True, read_only=True)
    genres = GenresSerializer(many=True, read_only=True)
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = models.Anime
        depth = 1
        fields = (
            'id', 'title', 'original_title', 'sinopse', 'release_date_of',
            'type_anime', 'genres', 'author', 'number_of_episodes', 'episodes'
        )
