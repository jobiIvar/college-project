from django.shortcuts import render, redirect
from .forms import AdmissionForm, PGAdmissionForm
from django.http import HttpResponseRedirect
from .models import CollegeAdmissionForm, PgAdmissionFormModel


# Create your views here.

def admission(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            admission_form = CollegeAdmissionForm()
            admission_form.name = form.cleaned_data.get('name')
            admission_form.email = form.cleaned_data.get('email')
            admission_form.phone_number = form.cleaned_data.get('phone_number')
            admission_form.dob = form.cleaned_data.get('dob')
            admission_form.gender = form.cleaned_data.get('gender')
            admission_form.qualification = form.cleaned_data.get('qualification')
            admission_form.address = form.cleaned_data.get('address')
            admission_form.landmark = form.cleaned_data.get('landmark')
            admission_form.state = form.cleaned_data.get('state')
            admission_form.pincode = form.cleaned_data.get('pincode')
            admission_form.photo = form.cleaned_data.get('photo')
            admission_form.signature = form.cleaned_data.get('signature')
            admission_form.sslc = form.cleaned_data.get('sslc')
            admission_form.hsc = form.cleaned_data.get('hsc')
            admission_form.aadhaar = form.cleaned_data.get('aadhaar')
            admission_form.community = form.cleaned_data.get('community')
            admission_form.transfer = form.cleaned_data.get('transfer')
            admission_form.conduct = form.cleaned_data.get('conduct')
            admission_form.verify = form.cleaned_data.get('verify')
            admission_form.save()
            return HttpResponseRedirect('/')

    form = AdmissionForm(request.POST)
    # print(form.is_valid())
    context = {"form": form}
    return render(request, 'admission.html', context)


def pg_admission(request):
    if request.method == 'POST':
        form = PGAdmissionForm(request.POST)
        if form.is_valid():
            admission_form = PgAdmissionFormModel()
            admission_form.name = form.cleaned_data.get('name')
            admission_form.email = form.cleaned_data.get('email')
            admission_form.phone_number = form.cleaned_data.get('phone_number')
            admission_form.dob = form.cleaned_data.get('dob')
            admission_form.gender = form.cleaned_data.get('gender')
            admission_form.qualification = form.cleaned_data.get('qualification')
            admission_form.address = form.cleaned_data.get('address')
            admission_form.landmark = form.cleaned_data.get('landmark')
            admission_form.state = form.cleaned_data.get('state')
            admission_form.pincode = form.cleaned_data.get('pincode')
            admission_form.photo = form.cleaned_data.get('photo')
            admission_form.signature = form.cleaned_data.get('signature')
            admission_form.sslc = form.cleaned_data.get('sslc')
            admission_form.hsc = form.cleaned_data.get('hsc')
            admission_form.aadhaar = form.cleaned_data.get('aadhaar')
            admission_form.community = form.cleaned_data.get('community')
            admission_form.transfer = form.cleaned_data.get('transfer')
            admission_form.conduct = form.cleaned_data.get('conduct')
            admission_form.degree_certificate = form.cleaned_data.get('degree_certificate')
            admission_form.provisional_certificate = form.cleaned_data.get('provisional_certificate')
            admission_form.verify = form.cleaned_data.get('verify')
            admission_form.save()
            return HttpResponseRedirect('/')

    form = PGAdmissionForm(request.POST)
    # print(form.is_valid())
    context = {"form": form}
    return render(request, 'admission.html', context)