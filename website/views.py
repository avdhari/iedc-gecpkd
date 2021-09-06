from django.shortcuts import render
from .models import *


def base_view(request):
    return render(request, 'website/base.html')


def home_view(request):
    events = Event.objects.all().order_by('-event_date')
    context = {
        "events": events
    }
    return render(request, 'website/index.html', context)


def event_view(request, pk):
    event = Event.objects.get(id=pk)
    context = {
        "event": event,
    }
    return render(request, 'website/event_detail.html', context)


def about_view(request):
    return render(request, 'website/about.html')