from django.shortcuts import render
from .models import Department, Courses, RankHolder, UniversityPlayer


# Create your views here.


def academics(request):
    department = Department.objects.all()
    context = {"department": department}
    return render(request, 'academics.html', context=context)


def course(request):
    mathematics = Courses.objects.filter(department__name="Mathematics")
    physics = Courses.objects.filter(department__name="Physics")
    tamil = Courses.objects.filter(department__name="Tamil")
    english = Courses.objects.filter(department__name="English")
    commerce = Courses.objects.filter(department__name="Commerce")
    business_administration = Courses.objects.filter(department__name="Business Administration")
    computer_science = Courses.objects.filter(department__name="Computer Science")
    zoology = Courses.objects.filter(department__name="Zoology")
    social_works = Courses.objects.filter(department__name="Social Works")
    physical_education = Courses.objects.filter(department__name="Physical Education")
    context = {'mathematics': mathematics,
               "physics": physics,
               "tamil": tamil,
               "english": english,
               "commerce": commerce,
               "business_administration": business_administration,
               "computer_science": computer_science,
               "zoology": zoology,
               "social_works": social_works,
               "physical_education": physical_education
               }
    return render(request, 'academics.html', context)


def rank_holder(request):
    rank_holders = RankHolder.objects.all()
    context = {"rank_holders": rank_holders}
    return render(request, 'academics.html', context)


def university_player(request):
    university_players = UniversityPlayer.objects.all()
    context = {"university_players": university_players}
    return render(request, "academics.html", context)
