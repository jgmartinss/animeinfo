from rest_framework import viewsets

from animeinfo.core import models

from . import serializers


class AnimeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AnimeSerializer
    queryset = models.Anime.objects.all().order_by('title')
