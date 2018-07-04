from django.shortcuts import render

def home(request):
	return render(request, "core/home.html", {})

def about(request):
    return render(request, "core/about.html", {})

def pastevent(request):
    return render(request, "core/pastevent.html", {})

def speakers(request):
    return render(request, "core/speakers.html", {})

def organizers(request):
    return render(request, "core/organizers.html", {})

def sponsors(request):
    return render(request, "core/sponsors.html", {})

def register(request):
    return render(request, "core/register.html", {})