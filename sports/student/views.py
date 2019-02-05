from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse

from django.contrib.auth import authenticate, login

from .models import Student

from django.views import View

from .forms import StudentCreationForm

class Student(View):
    form_class = StudentCreationForm
    initial = {}
    template_name = 'studentadd.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()

            return render(request, self.template_name, {'form': self.form_class(initial=self.initial) , "added" : True})


        return render(request, self.template_name, {'form': form , "error" : True})




