from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_cv, name='inicio_cv'),
]