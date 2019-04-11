
from django.contrib import admin

# Register your models here.

from .models import Event , Participate , Year , Position


admin.site.register(Event)
admin.site.register(Participate)
admin.site.register(Year)
admin.site.register(Position)
