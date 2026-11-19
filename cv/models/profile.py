from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    name = models.CharField(max_length=120)
    job_title = models.CharField(max_length=160)
    summary = models.TextField()
    photo = models.ImageField(upload_to="profile/", blank=True)
    email = models.EmailField()
    phone = PhoneNumberField(blank=True)
    location = models.CharField(max_length=120, blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")