from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator

class SkillCategory(models.Model):
    name = models.CharField(max_length=80)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = _("skill category")
        verbose_name_plural = _("skill categories")


class Skill(models.Model):
    category = models.ForeignKey(
        SkillCategory, on_delete=models.CASCADE, related_name="skills"
    )
    name = models.CharField(max_length=80)
    level = models.PositiveSmallIntegerField(
        default=50, validators=[MaxValueValidator(100)]
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["category__order", "order"]
        verbose_name = _("skill")
        verbose_name_plural = _("skills")