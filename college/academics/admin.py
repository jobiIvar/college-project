from django.contrib import admin
from .models import Courses, Department
# Register your models here.

admin.site.register(Department)
admin.site.register(Courses)