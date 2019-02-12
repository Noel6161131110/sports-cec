from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from django.contrib.auth import authenticate, login

from django.views import View

from .forms import UserCreationForm,UserLoginForm

from .models import User

from django.contrib.auth import logout

from django.contrib.auth.decorators import user_passes_test

from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


@method_decorator(user_passes_test(lambda u: u.is_superuser , login_url="/account/login?error=1") , name="dispatch" )
class SignupView(View):
    form_class = UserCreationForm
    initial = {}
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()

            return HttpResponseRedirect('/')


        return render(request, self.template_name, {'form': form , "error" : True})


class LoginView(View):
    form_class = UserLoginForm
    initial = {}
    template_name = 'login.html'
    def get(self,request):
        newuser = False
        if(request.GET.get("new",'0') == '1'):
            newuser = True
        login_req = False
        if(request.GET.get("login_req",'0') == '1'):
            login_req = True

        form = self.form_class(initial=self.initial)
        return render(request , "login.html" ,{"form" : form ,   "newuser" : newuser , "login_req" : login_req } )

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username',"")
        password = request.POST.get('password',"")
        if len(username) != 0 and len(password) != 0:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/")
        form = self.form_class(request.POST)
        return render(request, self.template_name, {'form': form , "error" : True})