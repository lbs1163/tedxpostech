from django.urls import path

from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pastevent/<int:year>/', views.pastevent, name='pastevent'),
    path('speakers/', views.speakers, name='speakers'),
    path('organizers/', views.organizers, name='organizers'),
    path('sponsors/', views.sponsors, name='sponsors'),
    path('register/', views.register, name='register'),
]