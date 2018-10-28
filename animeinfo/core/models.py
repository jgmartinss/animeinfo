from django.db import models

from django.utils.translation import ugettext_lazy as _


class Genres(models.Model):
    name = models.CharField(
        _('Name'), max_length=100, help_text=_('Example: Action, Comedy')
    )

    class Meta:
        verbose_name = _('Genres')
        verbose_name_plural = _('Genres')

    def __str__(self):
        return f'{self.name}'


class Author(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    date_of_birth = models.DateField(_('Date of birth'), blank=True, null=True)
    nationality = models.CharField(_('Nationality'), blank=True, max_length=100)
    about_of = models.TextField(_('About of'), blank=True)

    class Meta:
        db_table = 'tb_author'
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')

    def __str__(self):
        return f'{self.name}'


class Episode(models.Model):
    TYPE_EP = [
        ('canon', _('CANON')),
        ('filler', _('FILLER'))
    ]

    anime = models.ForeignKey(
        'core.Anime',
        verbose_name=_('Anime'),
        on_delete=models.CASCADE
    )
    title = models.CharField(_('Title'), max_length=140)
    original_title = models.CharField(_('Original title'), max_length=140)
    number_episode = models.PositiveSmallIntegerField(_('Number episode'))
    release_date_of = models.DateField(_('Release date of'))
    type_ep = models.CharField(_('Type episode'), max_length=6, choices=TYPE_EP)

    class Meta:
        db_table = 'tb_episode'
        verbose_name = _('Episode')
        verbose_name_plural = _('Episodes')

    def __str__(self):
        return f'{self.anime.title} EP {self.number_episode} - {self.title}'


class Anime(models.Model):
    TYPE_ANIME = [
        ('shounen', _('Shounen')),
        ('shoujo', _('Shoujo')),
        ('bishoujo', _('Bishoujo')),
        ('seinen', _('Seinen')),
        ('josei', _('Josei')),
        ('kodomo', _('Kodomo')),
        ('gekiga', _('Gekiga')),
        ('ecchi', _('Ecchi')),
        ('mahou shoujo', _('Mahou Shoujo')),
        ('mahou shounen', _('Mahou Shounen')),
        ('mecha', _('Mecha')),
        ('harem', _('Harém')),
        ('yaoi', _('Yaoi')),
        ('yuri', _('Yuri')),
        ('shotacon', _('Shotacon')),
        ('lolicon', _('Lolicon')),
        ('hentai', _('Hentai'))
    ]

    title = models.CharField(_('Title'), max_length=140)
    original_title = models.CharField(_('Original title'), max_length=140)
    sinopse = models.TextField(_('Sinopse'), blank=True)
    release_date_of = models.DateField(_('Release date of'))
    type_anime = models.CharField(_('Type'), max_length=50, choices=TYPE_ANIME)
    genres = models.ManyToManyField('core.Genres')
    author = models.ForeignKey(
        'core.Author',
        verbose_name=_('Author'),
        on_delete=models.CASCADE
    )
    episodes = models.ManyToManyField(
        'core.Episode',
        verbose_name=_('Episodes'),
        related_name='anime_episodes',
        blank=True
    )
    number_of_episodes = models.PositiveSmallIntegerField(
        _('Number of episodes'), blank=True, null=True
    )

    class Meta:
        db_table = 'tb_anime'
        verbose_name = _('Anime')
        verbose_name_plural = _('Animes')

    def __str__(self):
        return f'{self.title} - ({self.author})'
