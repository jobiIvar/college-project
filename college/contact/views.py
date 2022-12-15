from django.contrib import messages
from django.shortcuts import render
from .models import Contact


# Create your views here.

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        message = request.POST["message"]
        if (not name) or (not email) or (not phone_number) or (not message):
            messages.info(request, "Enter all the details")
        else:
            contact_message = Contact.objects.create(name=name, email=email, phone_number=phone_number, message=message)
            contact_message.save()
            messages.success(request, "Your Messages are Stored")

    return render(request, 'contact.html')
