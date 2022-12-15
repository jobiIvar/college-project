from django.shortcuts import render, HttpResponse
from .models import Event, Moto,Notification,Announcement
from academics.models import Department, RankHolder, UniversityPlayer
# Create your views here.

def home(request):
    events = Event.objects.all()
    mottos = Moto.objects.all()
    notifications = Notification.objects.all()
    announcements = Announcement.objects.all()
    departments = Department.objects.all()
    rank_holders = RankHolder.objects.filter(department=1)
    univ_players = UniversityPlayer.objects.all()
    context = {
        "events": events,
        "mottos": mottos,
        "notifications": notifications,
        "announcements": announcements,
        "departments": departments,
        "rank_holders": rank_holders,
        "univ_players": univ_players,
    }
    return render(request, 'index.html', context)
