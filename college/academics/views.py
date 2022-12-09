from django.shortcuts import render
from .models import Department, Courses


# Create your views here.


def academics(request):
    department = Department.objects.all()
    context = {"department": department}
    return render(request, 'academics.html', context=context)


def course(request):
    return render(request, 'academics.html')
