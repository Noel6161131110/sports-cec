from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse

from django.contrib.auth import authenticate, login

from django.conf import settings
from django.core.files.storage import FileSystemStorage


from .models import Student , ChestNo
from sportsbackend.models import Year , Participate

from django.views import View

from .forms import StudentCreationForm, ChestNumberUpdation

import csv


from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator


def process_admission_number(admno):
    if(len(admno) <= 3 ):return (-1,-1)
    if( admno.count("/") != 1  ):return (-1,-1)
    num , year = admno.split("/")
    try:
        num = int(num)
        if(len(year) == 4):
            year = year[2:]
        year = int(year)
    except:
        return (-1,-1)
    return (num,year)

@method_decorator(login_required(login_url="/account/login?error=1") , name="dispatch" )
class StudentAdd(View):
    form_class = StudentCreationForm
    initial = {}
    template_name = 'studentadd.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            admno , year = process_admission_number(form.cleaned_data["admission_number"])
            if(admno == -1):return render(request, self.template_name, {'form': form , "error" : True})
            name = form.cleaned_data["name"]
            if(Student.objects.filter(admission_number = admno , passout_year = year ).exists()):
                                Student.objects.filter(admission_number = admno , passout_year = year ).update(name = name , admission_number = admno , passout_year = year)
            else:
                Student(name = name , admission_number = admno , passout_year = year).save()
            return render(request, self.template_name, {'form': self.form_class(initial=self.initial) , "added" : True})


        return render(request, self.template_name, {'form': form , "error" : True})




@method_decorator(login_required(login_url="/account/login?error=1") , name="dispatch" )
class UploadCSV(View):

    def get(self, request, *args, **kwargs):
        return render(request, "csvupload.html")


    def post(self, request, *args, **kwargs):
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            with open("media/" + myfile.name) as csv_file:
                if(myfile.name[-3:] != "csv"):
                    return render(request , "csvupload.html" , {"error" : True})
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    for pos in range(len(row)):
                        admno , year = process_admission_number(row[pos])
                        if(admno != -1 ):
                            if(Student.objects.filter(admission_number = admno , passout_year = year ).exists()):
                                Student.objects.filter(admission_number = admno , passout_year = year ).update(name = row[pos+1] , admission_number = admno , passout_year = year)
                            else:
                                Student(name = row[pos+1] , admission_number = admno , passout_year = year).save()
            return render(request , "csvupload.html" , {"success" : True})


@method_decorator(login_required(login_url="/account/login?error=1") , name="dispatch" )
class CNo(View):
    form_class = ChestNumberUpdation
    initial = {}
    template_name = 'studentsno.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            admno , year = process_admission_number(form.cleaned_data["admission_number"])
            if(admno == -1):return render(request, self.template_name, {'form': form , "error" : True})
            if(Student.objects.filter(admission_number = admno , passout_year = year ).exists()):
                student = Student.objects.get(admission_number = admno , passout_year = year)
                yearobj = Year.objects.get(selected = True)
                cnobj = None
                if( ChestNo.objects.filter(student = student , year = yearobj ).exists() ):
                    ChestNo.objects.filter(student = student , year = yearobj).update(cno = form.cleaned_data["cno"])
                    cnobj = ChestNo.objects.get(student = student , year = yearobj)
                else:
                    cnobj = ChestNo(student = student , year = yearobj , cno = form.cleaned_data["cno"])
                    cnobj.save()
                Participate.objects.all().filter(student = student , year = yearobj).update(cno = cnobj  )
                return render(request , self.template_name , {'form' : form , "done" : True , "student" : student , "cno" : form.cleaned_data["cno"]})
            else:
                return render(request, self.template_name, {'form': form , "no" : True})
                
        return render(request, self.template_name, {'form': form , "error" : True})
