from django.urls import path
from . import views

urlpatterns = [
    path('', views.translate_file, name="translate_file"),
]
