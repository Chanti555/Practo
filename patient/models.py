from django.db import models


class Patient(models.Model):
    patid=models.IntegerField(primary_key=True)
    mobile= models.IntegerField()
    pswd = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    disease = models.CharField(max_length=20)
    symptoms = models.CharField(max_length=20)
    age = models.IntegerField()
    weight = models.IntegerField()
    gender = models.CharField(max_length=10)
    previousrecord = models.IntegerField()
    covidsymptoms = models.IntegerField()

def __str__(self):
    return str(self.mobilenumber)
