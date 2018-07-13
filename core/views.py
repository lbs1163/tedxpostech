from django.shortcuts import render
from .models import *

def home(request):
	return render(request, "core/home.html", {})

def about(request):
    return render(request, "core/about.html", {})

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
    return render(request, "core/sponsors.html", {})

def register(request):
    return render(request, "core/register.html", {})