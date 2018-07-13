from django.shortcuts import render
from .models import *
import datetime

def home(request):
    setting = Setting.objects.all().first()
    return render(request, "core/home.html", {'setting': setting})

def about(request):
    setting = Setting.objects.all().first()
    event = setting.event_now
    return render(request, "core/about.html", {'event': event})

def pastevent(request):
    return render(request, "core/pastevent.html", {})

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