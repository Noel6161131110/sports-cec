from django.shortcuts import render

from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

@login_required(login_url="/account/login?error=1") 
def dash(request):
    return render(request , "dash.html")