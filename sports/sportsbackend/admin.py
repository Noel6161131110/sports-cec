
from django.contrib import admin

# Register your models here.

from .models import Event , Participate , Year


admin.site.register(Event)
admin.site.register(Participate)
admin.site.register(Year)
