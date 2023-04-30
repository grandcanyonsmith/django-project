from django.urls import path
from . import views

urlpatterns = [
    path('submit_audio_url/', views.submit_audio_url, name='submit_audio_url'),
]
