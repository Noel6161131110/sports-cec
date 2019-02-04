from django.contrib import admin

# Register your models here.

from .models import Event , Participate , Year


admin.site.Register(Event)
admin.site.Register(Participate)
admin.site.Register(Year)
