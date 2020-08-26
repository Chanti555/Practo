from django.db import models

class Clinic(models.Model):
    clinicid = models.CharField(max_length=10, primary_key=True)
    pswd = models.CharField(max_length=20)
    clinicname = models.CharField(max_length=50)
    cityname = models.CharField(max_length=20)
    pincode = models.IntegerField()
    timein = models.TimeField()
    timeout = models.TimeField()
    mobile = models.IntegerField()
    noofdoctors = models.IntegerField()


def __str__(self):
        return str(self.clinicname)
