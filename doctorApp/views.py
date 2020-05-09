from django.shortcuts import render,redirect
from django.http import HttpResponse
from patientApp.models import Patient,Report
from django.forms import inlineformset_factory
from .forms import ReportForm
from datetime import datetime
# Create your views here.


def index(request):
    p=Patient.objects.all()
    print(p)
    return render(request,'doctorApp/listPatients.html',{
        'patients':p
    })

def showPatient(request,id):
    a=Patient.objects.get(pk=id)


    context={
        'details': a
    }
    print(a)
    return render(request,'doctorApp/showPatient.html',context=context)

def addreport(request,id):
    patient=Patient.objects.get(pk=id)
    
    if request.method=='POST':
        form=ReportForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            report=Report(reportfile=form.cleaned_data['reportfile'],dateCreated=datetime.today().strftime('%Y-%m-%d'),
            patient=patient)
            report.save()
            return redirect('docapp:showpatient',id=id)

    form=ReportForm()
    return render(request,'doctorApp/addreport.html',
    {
        'forms':form
    }
    )