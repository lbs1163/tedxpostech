from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import *
import datetime

def navbar_context_processor(request):
    setting = Setting.objects.all().first()
    past_events = Event.objects.filter(year__lt=setting.event_now.year).order_by('-year')
    return {'setting': setting, 'past_events': past_events}

def home(request):
    setting = Setting.objects.all().first()
    return render(request, "core/home.html", {'setting': setting})

def about(request):
    setting = Setting.objects.all().first()
    event = setting.event_now
    return render(request, "core/about.html", {'event': event})

def pastevent(request, year):
    setting = Setting.objects.all().first()
    if year >= setting.event_now.year:
        raise Http404()
    event = get_object_or_404(Event, year=year)
    organizers = event.organizer_set.all().order_by('name')
    speakers = event.speaker_set.all().order_by('published_datetime')
    sponsors = event.sponsors.all()
    return render(request, "core/pastevent.html", {'event': event, 'organizers': organizers, 'speakers': speakers, 'sponsors': sponsors})

def speakers(request):
    setting = Setting.objects.all().first()
    speakers = setting.event_now.speaker_set.all().order_by('published_datetime')
    return render(request, "core/speakers.html", {'setting': setting, 'speakers': speakers})

def organizers(request):
    setting = Setting.objects.all().first()
    organizers = setting.event_now.organizer_set.all().order_by('name')
    return render(request, "core/organizers.html", {'setting': setting, 'organizers': organizers})

def sponsors(request):
    setting = Setting.objects.all().first()
    sponsors = setting.event_now.sponsors.all()
    return render(request, "core/sponsors.html", {'setting': setting, 'sponsors': sponsors})

def register(request):
    setting = Setting.objects.all().first()
    event = setting.event_now
    t = ['월', '화', '수', '목', '금', '토', '일']
    day = t[event.date.weekday()]
    return render(request, "core/register.html", {'event': event, 'day': day})