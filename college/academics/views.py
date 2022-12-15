from django.shortcuts import render
from .models import Department, Courses, RankHolder, UniversityPlayer


# Create your views here.


def academics(request):
    department = Department.objects.all()
    context = {"department": department}
    return render(request, 'academics.html', context=context)


def course(request):
    courses = Courses.objects.all()
    context = {"courses": courses}
    return render(request, 'academics.html', context)


def rank_holder(request):
    rank_holders = RankHolder.objects.all()
    context = {"rank_holders": rank_holders}
    return render(request, 'academics.html', context)


def university_player(request):
    university_players = UniversityPlayer.objects.all()
    context = {"university_players": university_players}
    return render(request, "academics.html", context)