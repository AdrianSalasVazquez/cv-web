from django.db import models
from django.utils.translation import gettext_lazy as _
from .base import TimelineEntry

class Education(TimelineEntry):
    title = models.CharField(max_length=160)
    description = models.TextField(blank=True)

    class Meta(TimelineEntry.Meta):
        verbose_name = _("education")
        verbose_name_plural = _("education")