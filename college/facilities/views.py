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
