from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from doctor.models import doctor

def home(request):
    return render(request, 'home.html')


def docreg(request):
    return render(request, 'docreg.html')


def doclogin(request):
    return render(request, 'doclogin.html')


def docshowform(request):
    return render(request, 'docshowform.html')


def docupdateform(request):
    return render(request,'docupdateform.html')

def docdeleteform(request):
    return render(request,'docdeleteform.html')

def docregprocess(request):
    docID=request.GET.get('n1')
    pswd=request.GET.get('n2')
    name=request.GET.get('n3')
    speciality=request.GET.get('n4')
    exp=request.GET.get('n5')
    checkintime=request.GET.get('n6')
    checkouttime=request.GET.get('n7')
    clinicname=request.GET.get('n8')
    consultfee=request.GET.get('n9')
    mobile=request.GET.get('n10')
    about = request.GET.get('n11')

    try:
       rec=doctor.objects.get(ID=docID)
       return render(request,'doctregerror.html')
    except ObjectDoesNotExist:
        d1=doctor(docID,pswd,name,speciality,exp,checkintime,checkouttime,clinicname,consultfee,mobile,about)
        d1.save()
        return render(request,'doctregsuccess.html')

def doctshowprocess(request):
    docid=request.GET.get('n1')

    try:
       doc=doctor.objects.get(ID=docid)
       return render(request,"showdoct.html",{'docs':doc})
    except ObjectDoesNotExist:
        return render(request,'doctnotfound.html')

def doctlogin(request):
    docid=request.GET.get('n1')
    pswd=request.GET.get('n2')

    try:
       doc=doctor.objects.get(ID=docid,Pswd=pswd)
       return render(request,'doctloginsuccess.html')
    except ObjectDoesNotExist:
        return render(request,'doctloginerror.html')

def displayalldoctors(request):
    doc=doctor.objects.all()
    return render(request,"showalldoct.html",{'docs':doc})

def dispdoctbyname(request):
    docname=request.GET.get('n3')

    try:
       doc=doctor.objects.get(name=docname)
       return render(request,"showdoct.html",{'doc':docname})
    except ObjectDoesNotExist:
        return render(request,'doctnotfound.html')

def dispdoctbyclinic(request):
    docclinic=request.GET.get('n8')

    try:
       doc=doctor.objects.get(clinic=docclinic)
       return render(request,"showdoct.html",{'doc':docclinic})
    except ObjectDoesNotExist:
        return render(request,'doctnotfound.html')

def docteditprocess(request):
    docid = request.GET.get('n1')

    try:
       doc=doctor.objects.get(ID=docid)
       return render(request,"doctedit.html",{'doc':doc})
    except ObjectDoesNotExist:
        return render(request,'doctnotfound.html')

def doctupdate(request):
    docID = request.GET.get('n1')
    newpswd = request.GET.get('n2')
    newname = request.GET.get('n3')
    newspeciality = request.GET.get('n4')
    newexp = request.GET.get('n5')
    newcheckintime = request.GET.get('n6')
    newcheckouttime = request.GET.get('n7')
    newclinicname = request.GET.get('n8')
    newconsultfee = request.GET.get('n9')
    newmobile = request.GET.get('n10')
    newabout = request.GET.get('n11')

    d=doctor.objects.get(ID=docID)
    d.pswd=newpswd
    d.name=newname
    d.speciality = newspeciality
    d.exp = newexp
    d.checkintime = newcheckintime
    d.checkouttime = newcheckouttime
    d.consultfee = newconsultfee
    d.mobile = newmobile
    d.about = newabout

    d.save()
    return render(request,"doctupdatesuccess.html")

def doctdelete(request):
    docID=request.GET.get('n1')

    try:
        d=doctor.objects.get(ID=docID)
        d.delete()
        return render(request,'doctdeletesuccess.html')
    except ObjectDoesNotExist:
        return render(request,'doctnotfound.html')