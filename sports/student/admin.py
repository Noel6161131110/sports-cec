from django.contrib import admin

# Register your models here.

from .models import Student , ChestNo, DutyLeave

admin.site.register(Student)
admin.site.register(ChestNo)
admin.site.register(DutyLeave)
