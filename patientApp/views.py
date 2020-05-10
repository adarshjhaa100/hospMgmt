from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Patient,Report
from .forms import patientForm, userForm,reportForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.conf import settings

# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to patient app")

def pdfViewer(request,id):
    obj = Patient.objects.get(id=id)
    path = settings.MEDIA_ROOT
    context={
        'obj':obj,
        'path':path
    }
    return render(request,'patientApp/pdfViewer.html',context)


def deletePatient(request, id):
    if request.user.is_authenticated:
        obj = Patient.objects.get(id=id)
        if request.method == "POST":
            obj.delete()
            return redirect("../")
        context = {"obj": obj}
        return render(request, "patientApp/deletePatient.html", context)
    else:
        return HttpResponse("Unauthorized access")


def modifyPatient(request, id):
    if request.user.is_authenticated:
        obj = Patient.objects.get(id=id)
        if request.method == "POST":            
            form = patientForm(request.POST,request.FILES,instance=obj)
            if form.is_valid():
                form.save()
                return redirect("../")
        form = patientForm(None,instance=obj)
        context = {"form": form, "obj": obj}
        return render(request, "patientApp/updatePatient.html", context)
    else:
        return HttpResponse("Unauthorized access")


def listPatient(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            return redirect("add/")
        querySet = Patient.objects.all()
        context = {
            "objList": querySet,
        }
        return render(request, "patientApp/listPatient.html", context)
    else:
        return HttpResponse("Unauthorized access")


def addPatient(request):
    if request.user.is_authenticated:
        querySet = Patient.objects.all()
        print("hello world",request.method)
        if request.method=="POST":
            form = patientForm(request.POST,request.FILES)
            # print(form)
            if form.is_valid():
                form.save()
                form = patientForm()
                return redirect ('../')
        form = patientForm(None)
        context = {
            "form": form,
            "objList": querySet,
        }
        return render(request, "patientApp/listPatientAdd.html", context)
    else:
        return HttpResponse("Unauthorized access")


def loginPatientApp(request):
    form = userForm()
    if request.method == "POST":
        form = userForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("details/")
            else:
                return HttpResponse("Unauthorized access")
    context = {"form": form}
    return render(request, "patientApp/login.html", context)

def viewReport(request,id):
    # print(Report.objects.filter(patient__pk=id)[0].patient)
    context={
        'reports':Report.objects.filter(patient__pk=id),
        'patientName':Patient.objects.get(id=id).name
    }
    return render(request,'patientApp/viewReport.html',context)

def addReport(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = reportForm(request.POST, request.FILES)
            print(form)
            if form.is_valid():
                form.save()
                return redirect("patient:viewReport",Patient.objects.filter(name=form.cleaned_data['patient'])[0].id)
        form = reportForm(None)
        return render(request, "patientApp/addReport.html", {"form": form})
    else:
        return HttpResponse("Unauthorized access")

def deleteReport(request,id):
    if request.user.is_authenticated:
        obj = Report.objects.get(id=id)
        # print(Patient.objects.filter(name=obj.patient)[0].id)
        if request.method == "POST":
            obj.delete()
            return redirect("patient:viewReport",Patient.objects.filter(name=obj.patient)[0].id)
        context = {"report": obj}
        return render(request, "patientApp/deleteReport.html", context)
    else:
        return HttpResponse("Unauthorized access")

