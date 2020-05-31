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
    DEPARTMENT_CHOICES =[ 
            ('Accident and emergency (A&E)','Accident and emergency (A&E)'), 
            ('Admissions','Admissions'), 
            ('Breast Screening','Breast Screening'), 
            ('Burn Center','Burn Center'), 
            ('Cardiology','Cardiology'), 
            ('CSSD','Central Sterile Services Department (CSSD)'), 
            ('Chaplaincy','Chaplaincy'), 
            ('CCU','Coronary Care Unit'),
            ('Critical Care','Critical Care'),
            ('Diagnostic Imaging','Diagnostic Imaging'),
            ('Discharge Lounge','Discharge Lounge'),
            ('Elderly services','Elderly services'),
            ('Finance Department','Finance Department'),
            ('Gastroenterology','Gastroenterology'),
            ('General Services','General Services'),
            ('General Surgery','General Surgery'),
            ('Haematology','Haematology'),
            ('Health & Safety','Health & Safety'),
            ('ICU','Intensive Care Unit (ICU)'),
            ('Dental','Dental'),
            ('Opthalmologist','Opthalmologist')  
        ]
    name=models.CharField(default='defDoc',max_length=200)
    age=models.IntegerField(validators=[agevalidate],default=20)
    phone=models.CharField(default='1111111111',validators=[phonevalidate],max_length=12)
    licenseNo=models.CharField(default='1111111111',validators=[phonevalidate],max_length=12)
    address = models.TextField(blank=True, null=False)
    speciality=models.CharField(default='Health & Safety',null=False,max_length=100,
    choices=DEPARTMENT_CHOICES,
    )
    certificate=models.FileField('Certificate Add',upload_to='docCeritficates/')
    
    def __repr__(self):
        return self.name+'-'+self.licenseNo
    def __str__(self):
        return self.name+'-'+self.licenseNo


class PatientId(models.Model):
    pid=models.CharField(default='0',max_length=10)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)