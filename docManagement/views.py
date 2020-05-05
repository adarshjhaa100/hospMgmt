from django.shortcuts import render
from django.http import HttpResponse
from .forms import DoctorForm
from .models import Doctor
# Create your views here.

def index(request):

    return render(request,'docManagement/docOptions.html')

def addDoctor(request):
    if request.method=='POST':
        doc=DoctorForm(request.POST,request.FILES)
        print(doc)
        if doc.is_valid():
            print('yes')
            print(doc.cleaned_data)
            doc.save()
            return HttpResponse('Success Adding DOctor')
        else:
            return HttpResponse('Unsuccesful in adding docotor')    
    else:
        doc=DoctorForm()
        return render(request,'docManagement/addDoctor.html',{
            'docform':doc
        })
from django.views.decorators.clickjacking import xframe_options_sameorigin

@xframe_options_sameorigin
def showDoc(request):
    D=Doctor.objects.all()
    
    return render(request,"docManagement/showDoc.html",{
        'docList':D
    })