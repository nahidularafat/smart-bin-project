# ফাইল: main_app/urls.py (নতুন তৈরি করুন)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
]