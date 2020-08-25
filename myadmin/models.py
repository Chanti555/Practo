from django.db import models


class Myadmin(models.Model):
    userid = models.CharField(max_length=10, primary_key=True)
    pswd = models.CharField(max_length=20)


def __str__(self):
    return str(self.userid)
