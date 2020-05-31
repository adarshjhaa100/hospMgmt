from patientApp.models import Report, Patient
from docManagement.models import Doctor
from django import forms

class ReportForm(forms.ModelForm):
    class Meta:
        model=Report
        fields=[
            'reportfile',
            
        ]

class DocLogin(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=[
            'name',
            'licenseNo'
        ]