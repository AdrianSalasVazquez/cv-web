from django.db import models
from django.utils.translation import gettext_lazy as _

class Language(models.Model):
    LEVEL_CHOICES = [
        ("A1", "A1"),
        ("A2", "A2"),
        ("B1", "B1"),
        ("B2", "B2"),
        ("C1", "C1"),
        ("C2", "C2"),
        ("native", _("Native")),
    ]
    name = models.CharField(max_length=60)
    level = models.CharField(max_length=6, choices=LEVEL_CHOICES)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = _("language")
        verbose_name_plural = _("languages")