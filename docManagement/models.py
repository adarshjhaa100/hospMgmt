from django.db import models
from django.core.exceptions import ValidationError

def agevalidate(age):
    if(age<20 and age>80):
        return ValidationError('Invalid age')

def phonevalidate(ph):
    if(len(ph)<8 and len(ph)>12):
        return ValidationError('Invalid phone')



# Create your models here.
class Doctor(models.Model):
    DEPARTMENT_CHOICES=[
        ('General','General'),
        ('Opthalmologist','Opthalmologist'),
        ('OPD','OPD'),
        ('XRAY','XRAY'),
        ('Pathologist','Pathologist')
    ]
    name=models.CharField(default='defDoc',max_length=200)
    age=models.IntegerField(validators=[agevalidate],default=20)
    phone=models.CharField(default='1111111111',validators=[phonevalidate],max_length=12)
    licenseNo=models.CharField(default='1111111111',validators=[phonevalidate],max_length=12)
    address = models.TextField(blank=True, null=False)
    speciality=models.CharField(default="General",null=False,max_length=100,
    choices=DEPARTMENT_CHOICES,
    )
    certificate=models.FileField('Certificate Add',upload_to='docCeritficates/')
    
    def __repr__(self):
        return self.name+'-'+self.licenseNo
    def __str__(self):
        return self.name+'-'+self.licenseNo

