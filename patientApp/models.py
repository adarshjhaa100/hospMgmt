from django.db import models
from django.core.exceptions import ValidationError

# Validators
def ageValidate(age):
    if(age<20 and age>80):
        return ValidationError('Invalid age')

def aadharValidate(aadharNumber):
    if len(aadharNumber)!=12:
        return ValidationError('Enter a valid aadhar number')

def phoneValidate(ph):
    if(len(ph)<8 and len(ph)>12):
        return ValidationError('Invalid phone number')
# Create your models here.
class Patient(models.Model):
    name = models.CharField('Patient Name',max_length=120)  # max-field required
    age = models.IntegerField('Age',validators=[ageValidate])
    aadharNumber = models.CharField('Aadhar Number',max_length=12,validators=[aadharValidate],unique=True)
    BLOOD_GRP=[
        ('O+','O+'),
        ('A+','A+'),
        ('B+','B+'),
        ('AB+','AB+'),
        ('O-','O-'),
        ('A-','A-'),
        ('B-','B-'),
        ('AB-','AB-'),
    ]
    bloodGrp = models.CharField(
        'Blood group',
        max_length=3,
        choices=BLOOD_GRP,
        default='B+',
    )
    address = models.TextField('Address',blank=True, null=False)
    phoneNumber = models.CharField('Phone Number',max_length=15,validators=[phoneValidate])
    disease = models.CharField('Disease',max_length=30)
    createdDate = models.DateTimeField("Created", auto_now_add=True)
    modifiedDate = models.DateTimeField("Modified", auto_now=True)    
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
    diseaseType = models.CharField(
        max_length=30,
        choices=DEPARTMENT_CHOICES,
        default='Accident and emergency (A&E)',
    )

    def __repr__(self):
        return "<Patient %s>" % self.aadharNumber

    def __str__(self):
        return self.name


class Report(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    reportfile=models.FileField(upload_to='patientApp/')
    
    dateCreated=models.DateField(auto_now_add=True)