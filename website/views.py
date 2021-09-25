from django.shortcuts import render
from website.models import *
from website.tasks import image_url_split


def base_view(request):
    return render(request, 'website/base.html')


def home_view(request):
    events = Event.objects.all().order_by('-event_date')
    event = Event.objects.all()
    list_events = list(event)
    event_count = len(list_events)
    links_list = []
    for i in range(0, event_count):
        img_url = image_url_split(list_events[i].flyer)
        links_list.append(img_url)
    context = {
        "events": events,
        "links_list": links_list,
    }
    return render(request, 'website/index.html', context)


def event_view(request, slug):
    event = Event.objects.get(slug=slug)
    img_url = image_url_split(event.flyer)
    context = {
        "event": event,
        "img_url": img_url,
    }
    return render(request, 'website/event_detail.html', context)


def about_view(request):
    return render(request, 'website/about.html')