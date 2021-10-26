from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name="home-view"),
    path('base/', views.base_view, name="base-view"),
    path('events/<slug:slug>', views.event_view, name="event-view"),
    path('about/', views.about_view, name="about-view"),
    path('hustles/', views.hustle_chats, name="hustle-view"),
]
