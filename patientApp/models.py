from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=120)  # max-field required
    age = models.IntegerField()
    aadharNumber = models.IntegerField()
    bloodGrp = models.CharField(max_length=10)
    address = models.TextField(blank=True, null=False)
    phoneNumber = models.CharField(max_length=15)
    disease = models.CharField(max_length=15)
    createdDate = models.DateTimeField("Created", auto_now_add=True)
    modifiedDate = models.DateTimeField("Modified", auto_now=True)     
    def __repr__(self):
        return "<Patient %s>" % self.aadharNumber

    def __str__(self):
        return self.name

class Report(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    reportfile=models.FileField(upload_to='patientApp/')
    dateCreated=models.DateField(auto_now=False)