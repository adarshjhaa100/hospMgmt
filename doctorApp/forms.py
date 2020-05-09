from patientApp.models import Report, Patient
from django import forms

class ReportForm(forms.ModelForm):
    class Meta:
        model=Report
        fields=[
            'reportfile',
            
        ]
