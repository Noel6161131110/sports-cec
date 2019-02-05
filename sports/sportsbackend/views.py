from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse

from django.contrib.auth import authenticate, login

from .models import Event, Year, Participate

from django.views import View

from .forms import EventCreateForm, ParticipationForm

from student.views import process_admission_number

from student.models import Student

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
            event = form.save(commit=False)
            event.save()
            return render(request, self.template_name, {'form': self.form_class(initial=self.initial) , "added" : True})
        return render(request, self.template_name, {'form': form , "error" : True})



class CreateParticipation(View):

    form_class = ParticipationForm
    initial = {}
    template_name = 'participation.html'


    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            admno , year = process_admission_number(form.cleaned_data['admission_number'])
            if(Student.objects.filter(admission_number = admno , passout_year = year).exists()):
                student = Student.objects.get(admission_number = admno , passout_year = year)
                yearobj = Year.objects.get(selected = True)
                participate = form.save(commit=False)
                if(Participate.objects.filter(student = student , year = yearobj , event = participate.event ).exists() ):
                    return render(request, self.template_name, {'form': form , "repeat" : True})
                participate.student = student
                participate.year = yearobj
                participate.save()
                return render(request, self.template_name, {'form': self.form_class(initial=self.initial) , "added" : True , "student" : participate.student.name , "event" : participate.event.event_name  })
            return render(request, self.template_name, {'form': form , "error" : True})
        return render(request, self.template_name, {'form': form , "error" : True})

    