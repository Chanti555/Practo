from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from patient.models import Patient

def home(request):
    return render(request,'home.html')

def patientreg(request):
    return render(request,'patientreg.html')

def patloginform(request):
    return render(request,'patientlogin.html')

def patshowform(request):
    return render(request,'patientshowform.html')

def patupdateform(request):
    return render(request,'patientupdateform.html')

def patregprocess(request):
    patID=request.GET.get('n1')
    name=request.GET.get('n2')
    pswd=request.GET.get('n3')
    mobile=request.GET.get('n4')
    disease=request.GET.get('n5')
    symptoms=request.GET.get('n6')
    age=request.GET.get('n7')
    weight=request.GET.get('n8')
    gender=request.GET.get('n9')
    previousrecord=request.GET.get('n10')
    covidsymptoms= request.GET.get('n11')

    try:
       rec=Patient.objects.get(patid=patID)
       return render(request,'patregerror.html')
    except ObjectDoesNotExist:
        p1=Patient(patID,name,pswd,mobile,disease,symptoms,age,weight,gender,previousrecord,covidsymptoms)
        p1.save()
        return render(request,'patientregsuccess.html')

def doctshowprocess(request):
    patid=request.GET.get('n1')

    try:
       pat=Patient.objects.get(patid=patid)
       return render(request,"showpatient.html",{'pats':pat})
    except ObjectDoesNotExist:
        return render(request,'patientnotfound.html')

def patloginprocess(request):
    patid=request.GET.get('n1')
    pswd=request.GET.get('n3')

    try:
       pat=Patient.objects.get(patid=patid,p=pswd)
       return render(request,'patientloginsuccess.html')
    except ObjectDoesNotExist:
        return render(request,'patientloginerror.html')

def displayallpatients(request):
    pat=Patient.objects.all()
    return render(request,"showallpatient.html",{'pats':pat})

def pateditprocess(request):
    patid = request.GET.get('n1')

    try:
       pat=Patient.objects.get(ID=patid)
       return render(request,"patientedit.html",{'pats':pat})
    except ObjectDoesNotExist:
        return render(request,'patientnotfound.html')

def doctupdate(request):
    patID=request.GET.get('n1')
    newname=request.GET.get('n2')
    newpswd=request.GET.get('n3')
    newmobile=request.GET.get('n4')
    newdisease=request.GET.get('n5')
    newsymptoms=request.GET.get('n6')
    newage=request.GET.get('n7')
    newweight=request.GET.get('n8')
    newgender=request.GET.get('n9')
    newpreviousrecord=request.GET.get('n10')
    newcovidsymptoms= request.GET.get('n11')

    p=Patient.objects.get(patid=patID)
    p.name=newname
    p.pswd=newpswd
    p.mobile = newmobile
    p.disease = newdisease
    p.symptoms = newsymptoms
    p.age = newage
    p.weight = newweight
    p.gender = newgender
    p.previousrecord = newpreviousrecord
    p.covidsymptoms=newcovidsymptoms

    p.save()
    return render(request,"patientupdatesuccess.html")