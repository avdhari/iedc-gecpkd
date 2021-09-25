from django.urls import path
from .views import *


urlpatterns = [
    path('', home_view, name="home-view"),
    path('base/', base_view, name="base-view"),
    path('events/<slug:slug>', event_view, name="event-view"),
    path('about/', about_view, name="about-view")
]
