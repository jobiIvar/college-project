from django.shortcuts import render
from .models import Administration


# Create your views here.


def administration(request):
    return render(request, 'administration.html')


def principal(request):
    principal_info = Administration.objects.filter(position=1)
    context = {
        'principal_info': principal_info
    }
    print(principal_info)
    return render(request, "administration.html", context)


def correspondent(request):
    correspondent_info = Administration.objects.filter(position=2)
    context = {
        "correspondent_info": correspondent_info
    }
    return render(request, "administration.html", context)


def admin_board(request):
    administrative_board = Administration.objects.filter(position=4)
    context = {
        "administrative_board": administrative_board
    }
    return render(request, "administration.html", context)
