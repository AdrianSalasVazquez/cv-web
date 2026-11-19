from django.db import models
from django.utils.translation import gettext_lazy as _
from .skill import Skill

class Project(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/", blank=True)
    repo_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    technologies = models.ManyToManyField(Skill, blank=True, related_name="projects")
    order = models.PositiveIntegerField(default=0)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = _("project")
        verbose_name_plural = _("projects")