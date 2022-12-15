from django.shortcuts import render
from .models import Facility


# Create your views here.
def all(request):
    facilities = Facility.objects.all()
    context = {'facilities': facilities}
    return render(request, 'facilities.html', context=context)


def lab(request):
    labs = Facility.objects.filter(facility_type=1)
    context = {'labs': labs}
    return render(request, 'facilities.html', context=context)


def smart_class(request):
    smart_classes = Facility.objects.filter(facility_type=2)
    context = {"smart_classes": smart_classes}
    return render(request, "facilities.html", context=context)


def library(request):
    libraries = Facility.objects.filter(facility_type=3)
    context = {"libraries": libraries}
    return render(request, "facilities.html", context=context)


def sport(request):
    sports = Facility.objects.filter(facility_type=4)
    context = {"sports": sports}
    return render(request, "facilities.html", context)