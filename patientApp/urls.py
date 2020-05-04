from django.urls import include, path
from .views import (
    welcome,
    listPatient,
    addPatient,
    loginPatientApp,
    modifyPatient,
    deletePatient,
)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("details/delete/<int:id>", deletePatient, name="deletePatient"),
    path("details/modify/<int:id>", modifyPatient, name="modifyPatient"),
    path("", loginPatientApp, name="loginPatientApp"),
    path("details/add/", addPatient, name="addPatient"),
    path("details/", listPatient, name="listPatient"),
    path("welcome/", welcome, name="welcome"),
]
urlpatterns += staticfiles_urlpatterns()
