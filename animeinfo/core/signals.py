from django.db.models.signals import m2m_changed

from django.dispatch import receiver

from . import models


@receiver(m2m_changed, sender=models.Anime.episodes.through)
def episodes_total_handler(sender, instance, **kwargs):
    instance.number_of_episodes = instance.episodes.count()
    instance.save()
