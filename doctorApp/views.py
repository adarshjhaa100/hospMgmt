from django.shortcuts import render, redirect
from django.http import HttpResponse
from patientApp.models import Patient, Report
from django.forms import inlineformset_factory
from .forms import ReportForm,DocLogin
from datetime import datetime
from docManagement.models import Doctor

# Create your views here.

def docLogin(request):
    if(request.method=='POST'):
        form=DocLogin(request.POST)
        if(form.is_valid()):
            print(form.cleaned_data)
            fc=form.cleaned_data
            findDoc=Doctor.objects.filter(name=fc['name'],licenseNo=fc['licenseNo'])
            if(len(findDoc)>0):
                return redirect('docapp:docindex',id=findDoc[0].id)
            else:
                return redirect('docapp:doclogin')
    form=DocLogin()
    return render(request,'doctorApp/doclogin.html',{
        'form':form
    })


def index(request,id):
    d=Doctor.objects.get(pk=id)
    pList=[]
    
    for p in d.patientid_set.all():
        pList.append(Patient.objects.get(pk=p.pid))

    return render(request, 'doctorApp/listPatients.html', {
        'patients': pList,
        'doc':d

    })


def showPatient(request, id,did):
    a = Patient.objects.get(pk=id)
    d=Doctor.objects.get(pk=did)
  
    context = {
        'details': a,
        'docid':d.id
    }
    print(a)
    return render(request, 'doctorApp/showPatient.html', context=context)


def addreport(request,id,did):
    patient = Patient.objects.get(pk=id)

    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        print(form)
        
        if form.is_valid():
            report = Report(reportfile=form.cleaned_data['reportfile'], dateCreated=datetime.today().strftime('%Y-%m-%d'),
                            patient=patient)
            report.save()
            return redirect('docapp:showpatient', id=id,did=did)

    form = ReportForm()
    return render(request, 'doctorApp/addreport.html',
                  {
                      'forms': form
                  }
                  )
