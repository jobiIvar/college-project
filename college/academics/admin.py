from django.contrib import admin
from .models import Courses, Department,RankHolder, UniversityPlayer
# Register your models here.

admin.site.register(Department)
admin.site.register(Courses)
admin.site.register(RankHolder)
admin.site.register(UniversityPlayer)
