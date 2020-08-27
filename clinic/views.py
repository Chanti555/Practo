from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from clinic.models import Clinic

def clinicreg(request):
    return render(request, 'clinicreg.html')

def clinicloginform(request):
    return render(request, 'cliniclogin.html')

def clinicshowform(request):
    return render(request, 'clinicshowform.html')

def clinicupdateform(request):
    return render(request, 'clinicupdateform.html')

def clinicdeleteform(request):
    return render(request, 'clinicdeleteform.html')

def searchclinic(request):
    return render(request, 'searchclinic.html')

def clinicregprocess(request):
    clinicID = request.GET.get('n1')
    pswd = request.GET.get('n2')
    clinicname = request.GET.get('n3')
    cityname = request.GET.get('n4')
    pincode = request.GET.get('n5')
    timein = request.GET.get('n6')
    timeout = request.GET.get('n7')
    mobile = request.GET.get('n8')
    noofdoctors = request.GET.get('n9')

    try:
       rec=Clinic.objects.get(clinicid=clinicID)
       return render(request,'clinicregerror.html')
    except ObjectDoesNotExist:
        c1=Clinic(clinicID,pswd,clinicname,cityname,pincode,timein,timeout,mobile,noofdoctors)
        c1.save()
        return render(request,'clinicregsuccess.html')

def clinicshowprocess(request):
    clinicid=request.GET.get('n1')

    try:
       clin=Clinic.objects.get(cliniid=clinicid)
       return render(request,"showclinic.html",{'clinics':clin})
    except ObjectDoesNotExist:
        return render(request,'clinicnotfound.html')

def cliniclogin(request):
    clinicid=request.GET.get('n1')
    pswd=request.GET.get('n2')

    try:
       clin=Clinic.objects.get(clinicid=clinicid,pswd=pswd)
       return render(request,'clinicloginsuccess.html')
    except ObjectDoesNotExist:
        return render(request,'clinicloginerror.html')

def displayallclinics(request):
    clin=Clinic.objects.all()
    return render(request,"showallclinics.html",{'clinics':clin})

def dispclinicbycity(request):
    clinicity=request.GET.get('n4')

    try:
       clin=Clinic.objects.get(cityname=clinicity)
       return render(request,"showclinic.html",{'clinic':clin})
    except ObjectDoesNotExist:
        return render(request,'clinicnotfound.html')

def dispclinicbyname(request):
    clinicname=request.GET.get('n3')

    try:
       clin=Clinic.objects.get(clinic=clinicname)
       return render(request,"showclinic.html",{'clinic':clin})
    except ObjectDoesNotExist:
        return render(request,'clinicnotfound.html')

def cliniceditprocess(request):
    clinicid = request.GET.get('n1')

    try:
       clin=Clinic.objects.get(ID=clinicid)
       return render(request,"clinicedit.html",{'clinic':clin})
    except ObjectDoesNotExist:
        return render(request,'clinicnotfound.html')

def clinicupdate(request):
    clinicID = request.GET.get('n1')
    newpswd = request.GET.get('n2')
    newclinicname = request.GET.get('n3')
    newcityname = request.GET.get('n4')
    newpincode = request.GET.get('n5')
    newtimein = request.GET.get('n6')
    newtimeout = request.GET.get('n7')
    newmobile = request.GET.get('n8')
    newnoofdoctors = request.GET.get('n9')

    c=Clinic.objects.get(clinicid=clinicID)
    c.pswd=newpswd
    c.name=newclinicname
    c.cityname= newcityname
    c.pincode = newpincode
    c.timein = newtimein
    c.timeout = newtimeout
    c.mobile = newmobile
    c.noofdoctors = newnoofdoctors

    c.save()
    return render(request,"clinicupdatesuccess.html")

def clinicdelete(request):
    clinicID=request.GET.get('n1')

    try:
        c=Clinic.objects.get(clinicid=clinicID)
        c.delete()
        return render(request,'clinicdeletesuccess.html')
    except ObjectDoesNotExist:
        return render(request,'clinicnotfound.html')