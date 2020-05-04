from django.db import models

from django.core.exceptions import ValidationError

#validator
def userValidate(name):
    if(len(name)<5):
        raise ValidationError('username should be more than 5 characters long')


# Create your models here.
class myUser(models.Model):
    username=models.CharField(unique=True,validators=[userValidate],max_length=32)
    password=models.CharField(max_length=32)
    logged_in=models.BooleanField(default=False)

    def __str__(self):
        return self.username