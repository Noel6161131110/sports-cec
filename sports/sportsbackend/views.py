from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse

from django.contrib.auth import authenticate, login

from .models import Event

from django.views import View

from .forms import EventCreateForm, ParticipationForm

class Event(View):
    form_class = EventCreateForm
    initial = {}
    template_name = 'eventadd.html'

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



class Participation(View):

    form_class = ParticipationForm
    initial = {}
    template_name = 'participation.html'


    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

		
    def post(self, request, *args, **kwargs):
		pass
