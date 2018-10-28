from django.contrib import admin

from django.utils.translation import gettext_lazy as _

from . import models


class EpisodeInline(admin.TabularInline):
    model = models.Episode

    extra = 2
    fields = (
        'title', 'original_title',
        'number_episode', 'type_ep',
        'release_date_of'
    )


class EpisodeAdmin(admin.ModelAdmin):
    model = models.Episode

    list_display = [
        'anime' ,'title', 'number_episode',
        'type_ep', 'release_date_of'
    ]
    ordering = ('title',)
    list_display_links = ['title']
    search_fields = ('title', 'anime__title',)
    list_filter = ('type_ep', 'anime__title',)
    fieldsets = (
        (None, {
            'fields': (
                'anime',
                ('title', 'original_title',),
                ('number_episode', 'type_ep',),
                'release_date_of',
            ),
        }),
    )


class AnimeAdmin(admin.ModelAdmin):
    model = models.Anime

    list_display = [
        'title', 'type_anime', 'get_genres',
        'number_of_episodes', 'release_date_of',
    ]
    ordering = ('title',)
    list_display_links = ['title']
    search_fields = ('title', 'author__name')
    list_filter = ('type_anime', 'author__name',)
    inlines = (EpisodeInline,)
    fieldsets = (
        (None, {
            'fields': (
                'author', 'title', 'original_title',
                ('type_anime', 'genres'),
                'release_date_of', 'episodes',
                'number_of_episodes',
            ),
        }),
    )

    def get_genres(self, obj):
        return "\n".join([
            g.name for g in obj.genres.all()
        ])
    get_genres.short_description = _("Genres")


class AuthorAdmin(admin.ModelAdmin):
    model = models.Author

    list_display = ['name', 'date_of_birth', 'nationality']
    ordering = ('name',)
    list_display_links = ['name']
    search_fields = ('name',)
    fieldsets = (
        (None, {
            'fields': (
                'name', 'about_of',
                ('date_of_birth', 'nationality',),
            ),
        }),
    )


class GenresAdmin(admin.ModelAdmin):
    model = models.Genres

    list_display = ['name']
    ordering = ('name',)
    list_display_links = ['name']
    search_fields = ('name',)


admin.site.register(models.Anime, AnimeAdmin)
admin.site.register(models.Episode, EpisodeAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Genres, GenresAdmin)
