from django import forms
from .models import Patient

# from django.contrib.auth.models import User
class patientForm(forms.ModelForm):
    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "style": "border-color: blue;",
                "placeholder": "Write your title here",
                "class": "form-control",
            }
        ),
    )
    address = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Write your address here",
                "style": "border-color: orange;",
                "class": "form-control",
            }
        ),
    )

    class Meta:
        model = Patient
        fields = [
            "name",
            "age",
            "aadharNumber",
            "bloodGrp",
            "address",
            "phoneNumber",
            "disease",
            # "patientImgReport",
            # "createdDate",
            # "modifiedDate",
        ]


class userForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"name": "username", "class": "form-control"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"name": "password", "class": "form-control"})
    )
