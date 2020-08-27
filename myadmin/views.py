from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from myadmin.models import Myadmin


def adminreg(request):
    return render(request, 'adminreg.html')


def adminregprocess(request):
    aid = request.GET.get('n1')
    apin = request.GET.get('n2')

    try:
        doc = Myadmin.objects.get(userid=aid, pswd=apin)
        return render(request, 'adminloginsuccess.html')
    except ObjectDoesNotExist:
        return render(request, 'adminloginerror.html')
