from django.urls import include, path
from .views import (
    welcome,
    listPatient,
    addPatient,
    loginPatientApp,
    modifyPatient,
    deletePatient,
    pdfViewer,
    viewReport
)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # Report URLS
    path('viewReport/<int:id>',viewReport,name='viewReport'),
    # Patient URLS    
    path('pdfviewer/<int:id>',pdfViewer,name='pdfViewer'),
    path("details/delete/<int:id>", deletePatient, name="deletePatient"),
    path("details/modify/<int:id>", modifyPatient, name="modifyPatient"),
    path("", loginPatientApp, name="loginPatientApp"),
    path("details/add/", addPatient, name="addPatient"),
    path("details/", listPatient, name="listPatient"),
    path("welcome/", welcome, name="welcome"),
]
urlpatterns += staticfiles_urlpatterns()
