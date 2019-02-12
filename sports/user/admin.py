from django.contrib import admin

# Register your models here.

from .models import User

class UserFilter(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_superuser=False)

admin.site.site_header = "Cec Sports Server ";
admin.site.site_title = "CEC ";

admin.site.register(User,UserFilter)
