from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Patient
from .forms import patientForm, userForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to patient app")


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
        form = patientForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("../")
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
        form = patientForm(request.POST or None)
        print(request.user)
        querySet = Patient.objects.all()
        if form.is_valid():
            form.save()
            form = patientForm()
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
