from django.db import models
from django.utils.translation import gettext_lazy as _


class TimelineEntry(models.Model):
    """Campos compartidos para experience y education"""
    organization = models.CharField(max_length=120)
    organization_url = models.URLField(blank=True)
    logo = models.ImageField(upload_to="logos/", blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ["-start_date"]

    @property
    def is_current(self):
        return self.end_date is None