from django.shortcuts import render
from website.models import *
from website.tasks import image_url_split


def base_view(request):
    return render(request, 'website/base.html')


def home_view(request):
    events = Event.objects.all().order_by('-event_date')
    list_events = list(events)
    event_count = Event.objects.all().count()
    links_list = []
    for i in range(event_count):
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
    nodal_officer = NodalOfficer.objects.all()
    team_members = TeamMember.objects.all()
    context = {
        'nodal_officer': nodal_officer,
        'team_members': team_members,
    }
    return render(request, 'website/about.html', context)


def hustle_chats(request):
    videos = HustleChat.objects.all()
    context = {
        'videos': videos,
    }
    return render(request, 'website/hustle_chats.html', context)