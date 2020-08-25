from django.db import models
# Create your models here.
class Appointment(models.Model):
    appid=models.CharField(max_length=10 , primary_key=True)
    appbypatient = models.CharField(max_length=20)
    apptodoctor= models.CharField(max_length=20)
    apptime = models.TimeField()
    status = models.CharField(max_length=30)
    def __str__(self):
        return str(self.appid)
