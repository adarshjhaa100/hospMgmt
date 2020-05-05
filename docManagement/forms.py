from .models import Doctor
from django.forms import ModelForm

class DoctorForm(ModelForm):
    class Meta:
        model=Doctor
        fields=['name','age','phone','licenseNo','address','speciality','certificate']
