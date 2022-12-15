from django.contrib import admin
from .models import Event, Moto,Notification, Announcement
# Register your models here.
admin.site.register(Event)
admin.site.register(Moto)
admin.site.register(Notification)
admin.site.register(Announcement)
