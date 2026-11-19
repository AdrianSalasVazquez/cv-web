from django.db import models
from django.utils.translation import gettext_lazy as _
from .base import TimelineEntry

class Experience(TimelineEntry):
    position = models.CharField(max_length=120)

    class Meta(TimelineEntry.Meta):
        verbose_name = _("experience")
        verbose_name_plural = _("experience")


class ExperiencePoint(models.Model):
    experience = models.ForeignKey(
        Experience, on_delete=models.CASCADE, related_name="points"
    )
    text = models.CharField(max_length=300)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]