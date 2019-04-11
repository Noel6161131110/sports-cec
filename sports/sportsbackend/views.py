from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse

from django.contrib.auth import authenticate, login

from .models import Event, Year, Participate , Position

from django.views import View

from .forms import EventCreateForm, ParticipationForm, EventSelectForm, AdmissionNumberForm , StudentReportForm, YearSelectForm

from student.views import process_admission_number

from student.models import Student, ChestNo

from django.db.models import Max


from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

@method_decorator(login_required(login_url="/account/login?error=1") , name="dispatch" )
class AddEvent(View):
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


@method_decorator(login_required(login_url="/account/login?error=1") , name="dispatch" )
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
                cobj = None
                if( ChestNo.objects.filter(student = student , year = yearobj).exists() ):
                    cobj = ChestNo.objects.get(student = student , year = yearobj)
                if(Participate.objects.filter(student = student , year = yearobj , event = participate.event  ).exists() ):
                    return render(request, self.template_name, {'form': form , "repeat" : True})
                participate.student = student
                participate.year = yearobj
                participate.cno = cobj
                participate.pos = Position.objects.get(position = "Registered")
                participate.save()
                return render(request, self.template_name, {'form': self.form_class(initial=self.initial) , "added" : True , "student" : participate.student.name , "event" : participate.event.event_name  })
            return render(request, self.template_name, {'form': form , "error" : True})
        return render(request, self.template_name, {'form': form , "error" : True})



@method_decorator(login_required(login_url="/account/login?error=1") , name="dispatch" )
class ConfirmParticipationSelect(View):

    form_class = EventSelectForm
    second_form_class = AdmissionNumberForm
    initial = {}
    template_name = 'participationverifyselect.html'
    second_template_name = 'participationverify.html'

    def get(self, request, *args, **kwargs):
        if(request.GET.get("event",0) == 0):
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})
        form = self.form_class(request.GET)
        if form.is_valid():
            participate = form.save(commit=False)
            yearobj = Year.objects.get(selected = True)
            participateobjs = Participate.objects.all().filter(event = participate.event , year = yearobj ).order_by('-pos')
            if(participateobjs.count() == 0 ):
                return render(request, self.template_name, {'form': form , "error" :True})
            form = self.second_form_class(initial=self.initial)
            return render(request , self.second_template_name , { "year" : yearobj , "data" : participateobjs , "form" : form ,  "event" : participate.event.id  , "eventname" :participate.event.event_name})


    
    def post(self, request, *args, **kwargs):
        form = self.second_form_class(request.POST)
        if form.is_valid():
            admno , year = process_admission_number(form.cleaned_data['admission_number'])
            eventid = request.POST.get("event",0)
            eventobj = Event.objects.get(id = eventid)
            yearobj = Year.objects.get(selected = True)
            participateobjs = Participate.objects.all().filter(event = eventobj , year = yearobj ).order_by('-pos')
            if(Student.objects.filter(admission_number = admno , passout_year = year).count() == 0):
                return render(request , self.second_template_name , {"data" : participateobjs , "form" : form , "event" : eventid , "eventname" : eventobj.event_name , "error2" : True})                
            student = Student.objects.get(admission_number = admno , passout_year = year)
            participateobj = participateobjs.filter(student = student)
            participateobj.update(pos = form.cleaned_data['pos'])
            return render(request , self.second_template_name , {"year" : yearobj ,"data" : participateobjs , "form" : form  , "event" : eventid , "eventname" : eventobj.event_name})


@method_decorator(login_required(login_url="/account/login?error=1") , name="dispatch" )
class StudentReport(View):
    form_class = StudentReportForm
    initial = {}
    template_name = 'selectstudentreport.html'
    second_template_name = 'studentreport.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            admno , year = process_admission_number(form.cleaned_data['admission_number'])
            if (Student.objects.filter(admission_number = admno , passout_year = year).count() == 0):
                form = self.form_class(initial=self.initial)
                return render(request, self.template_name, {'form': form , "error" : True})
            student =Student.objects.get(admission_number = admno , passout_year = year)
            participateobjs = Participate.objects.all().filter(student = student )
            return render(request,self.second_template_name , {"data" : participateobjs , 'student' : student})


@method_decorator(login_required(login_url="/account/login?error=1") , name="dispatch" )
class Disqualify(View):

    form_class = ParticipationForm
    initial = {}
    template_name = 'disqualify.html'
    second_template_name = 'disqualifyconfirm.html'

    def get(self, request, *args, **kwargs):
        if(request.GET.get("event",0) == 0):
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})
        form = self.form_class(request.GET)
        if form.is_valid():
            admno , year = process_admission_number(form.cleaned_data['admission_number'])
            participate = form.save(commit=False)
            if(Student.objects.filter(admission_number = admno , passout_year = year).exists() == False):
                return render(request, self.template_name, {'form': form , "no" : True})         
            student = Student.objects.get(admission_number = admno , passout_year = year)
            yearobj = Year.objects.get(selected = True)
            participateobjs = Participate.objects.filter(student = student , year = yearobj , event = participate.event )
            if(participateobjs.exists()):
                return render(request , self.second_template_name , {"student" : student , "event" : participate.event } ) 
        return render(request, self.template_name, {'form': form , "error" : True})         


    def post(self, request, *args, **kwargs):
        eventid = request.POST.get("event" , 0)
        studentid = request.POST.get("student" , 0)
        if(eventid == 0 or studentid == 0):
            return HttpResponseRedirect("/app/disqualify")
        student  = Student.objects.get(id = studentid)
        event = Event.objects.get(id = eventid)
        yearobj = Year.objects.get(selected = True)
        
        Participate.objects.all().filter(student = student , year = yearobj , event = event).delete()

        #for i in range(1,4):
        #    if(Participate.objects.all().filter(  year = yearobj , event = event , position = i).count() > 0):
        #        continue
        #    Participate.objects.all().filter(  year = yearobj , event = event , position = i+1).update(position = i)
        
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form , "removed" : True})


@method_decorator(login_required(login_url="/account/login?error=1") , name="dispatch" )
class EventReport(View):

    form_class = EventSelectForm
    initial = {}
    template_name = 'reportselectevent.html'
    second_template_name = 'eventreport.html'

    def get(self, request, *args, **kwargs):
        if(request.GET.get("event",0) == 0):
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})
       
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            participate = form.save(commit=False)
            yearobj = Year.objects.get(selected = True)
            participateobjs = Participate.objects.all().filter(event = participate.event , year = yearobj ).order_by('pos')
            if(participateobjs.count() == 0 ):
                return render(request, self.template_name, {'form': form , "error" :True})
            return render(request , self.second_template_name , { "year" : yearobj , "data" : participateobjs , "eventname" : participate.event.event_name })


@method_decorator(login_required(login_url="/account/login?error=1") , name="dispatch" )
class TrackCard(View):

    form_class = EventSelectForm
    initial = {}
    template_name = 'trackselect.html'
    second_template_name = 'scorecardtrack.html'

    def get(self, request, *args, **kwargs):
        if(request.GET.get("event",0) == 0):
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})
       
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            participate = form.save(commit=False)
            yearobj = Year.objects.get(selected = True)
            participateobjs = Participate.objects.all().filter(event = participate.event , year = yearobj )
            if(participateobjs.count() == 0 ):
                return render(request, self.template_name, {'form': form , "error" :True})
            return render(request , self.second_template_name , { "year" : yearobj , "data" : participateobjs , "eventname" : participate.event.event_name })

@method_decorator(login_required(login_url="/account/login?error=1") , name="dispatch" )
class FieldCard(View):

    form_class = EventSelectForm
    initial = {}
    template_name = 'fieldselect.html'
    second_template_name = 'scorecardfield.html'

    def get(self, request, *args, **kwargs):
        if(request.GET.get("event",0) == 0):
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})
       
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            participate = form.save(commit=False)
            yearobj = Year.objects.get(selected = True)
            participateobjs = Participate.objects.all().filter(event = participate.event , year = yearobj ).order_by('-pos')
            if(participateobjs.count() == 0 ):
                return render(request, self.template_name, {'form': form , "error" :True})
            return render(request , self.second_template_name , { "year" : yearobj , "data" : participateobjs , "eventname" : participate.event.event_name })


class SelectYear(View):
    form_class = YearSelectForm
    initial = {}
    template_name = 'yearselect.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        yearobj = Year.objects.get(selected = True)
        return render(request, self.template_name, {'form': form , "year" : yearobj})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            year = form.cleaned_data["year"]
            if(Year.objects.filter(year = year).exists() == False):
                Year(year = year).save()
            Year.objects.all().update(selected = False)
            Year.objects.filter(year=year).update(selected=True)
            return HttpResponseRedirect("/app/selectyear")