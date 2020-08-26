from django.db import models

class Doctor(models.Model):
    doctid = models.CharField(max_length=10, primary_key=True)
    pswd = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    speciality = models.CharField(max_length=20)
    exp = models.IntegerField
    checkintime = models.TimeField(max_length=20)
    checkouttime = models.TimeField(max_length=10)
    clinicname = models.CharField(max_length=30)
    consultfee = models.IntegerField()
    mobile = models.IntegerField()
    about = models.CharField(max_length=50)

def __str__(self):
    return str(self.name)
