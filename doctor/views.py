from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from doctor.models import Doctor

def docshowform(request):
    return render(request,'docshowform.html')

def docreg(request):
    return render(request, 'docreg.html')

def docloginform(request):
    return render(request, 'doclogin.html')

def searchdoc(request):
    return render(request, 'searchdoc.html')

def docupdateform(request):
    return render(request,'docupdateform.html')

def docdeleteform(request):
    return render(request,'docdeleteform.html')

def docregprocess(request):
    docID=request.GET.get('n1')
    pswd=request.GET.get('n2')
    name=request.GET.get('n3')
    speciality=request.GET.get('n4')
    expyear=request.GET.get('n5')
    checkintime=request.GET.get('n6')
    checkouttime=request.GET.get('n7')
    clinicname=request.GET.get('n8')
    consultfee=request.GET.get('n9')
    mobile=request.GET.get('n10')
    about = request.GET.get('n11')

    try:
       rec=Doctor.objects.get(doctid=docID)
       return render(request,'adminregerror.html')
    except ObjectDoesNotExist:
        d1=Doctor(doctid=docID,pswd=pswd,name=name,speciality=speciality,expyear=expyear,checkintime=checkintime,checkouttime=checkouttime,clinicname=clinicname,consultfee=consultfee,mobile=mobile,about=about)
        d1.save()
        return render(request,'adminregsuccess.html')

def docshowprocess(request):
    docid=request.GET.get('n1')

    try:
       doc=Doctor.objects.get(doctid=docid)
       return render(request,"showdoc.html",{'docs':doc})
    except ObjectDoesNotExist:
        return render(request,'docnotfound.html')

def doclogin(request):
    docid=request.GET.get('n1')
    pswd=request.GET.get('n2')

    try:
       doc=Doctor.objects.get(doctid=docid,pswd=pswd)
       return render(request,'patientloginsuccess.html')
    except ObjectDoesNotExist:
        return render(request,'patientloginerror.html')

def displayalldoctors(request):
    doc=Doctor.objects.all()
    return render(request,"showalldoc.html",{'docs':doc})

def dispdocbyname(request):
    docname=request.GET.get('n3')

    try:
       doc=Doctor.objects.get(name=docname)
       return render(request,"showdoc.html",{'doc':docname})
    except ObjectDoesNotExist:
        return render(request,'docnotfound.html')

def dispdocbyclinic(request):
    docclinic=request.GET.get('n8')

    try:
       doc=Doctor.objects.get(clinicname=docclinic)
       return render(request,"showdoc.html",{'doc':docclinic})
    except ObjectDoesNotExist:
        return render(request,'docnotfound.html')

def doceditprocess(request):
    docid = request.GET.get('n1')

    try:
       doc=Doctor.objects.get(docid=docid)
       return render(request,"docedit.html",{'doc':doc})
    except ObjectDoesNotExist:
        return render(request,'docnotfound.html')

def docupdate(request):
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

    d=Doctor.objects.get(docid=docID)
    d.pswd=newpswd
    d.name=newname
    d.speciality = newspeciality
    d.expyear = newexp
    d.checkintime = newcheckintime
    d.checkouttime = newcheckouttime
    d.consultfee = newconsultfee
    d.mobile = newmobile
    d.about = newabout

    d.save()
    return render(request,"doctupdatesuccess.html")

def docdelete(request):
    docID=request.GET.get('n1')

    try:
        d=Doctor.objects.get(docid=docID)
        d.delete()
        return render(request,'docdeletesuccess.html')
    except ObjectDoesNotExist:
        return render(request,'docnotfound.html')