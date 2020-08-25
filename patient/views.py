from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from patients.models import Patient

def home(request):
    return render(request,'home.html')

def patregform(request):
    return render(request,'patreg.html')

def patloginform(request):
    return render(request,'patlogin.html')

def patshowform(request):
    return render(request,'patshowform.html')

def patupdateform(request):
    return render(request,'patupdateform.html')

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
       rec=patient.objects.get(ID=patID)
       return render(request,'patregerror.html')
    except ObjectDoesNotExist:
        p1=patient(patID,name,pswd,mobile,disease,symptoms,age,weight,gender,previousrecord,covidsymptoms)
        p1.save()
        return render(request,'doctregsuccess.html')

def doctshowprocess(request):
    patid=request.GET.get('n1')

    try:
       pat=patient.objects.get(ID=patid)
       return render(request,"showpat.html",{'pats':pat})
    except ObjectDoesNotExist:
        return render(request,'patnotfound.html')

def patloginprocess(request):
    patid=request.GET.get('n1')
    pswd=request.GET.get('n3')

    try:
       pat=patient.objects.get(ID=patid,Pswd=pswd)
       return render(request,'patloginsuccess.html')
    except ObjectDoesNotExist:
        return render(request,'patloginerror.html')

def displayallpatients(request):
    pat=patient.objects.all()
    return render(request,"showallpat.html",{'pats':pat})

def pateditprocess(request):
    patid = request.GET.get('n1')

    try:
       pat=patient.objects.get(ID=patid)
       return render(request,"patedit.html",{'pats':pat})
    except ObjectDoesNotExist:
        return render(request,'patnotfound.html')

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

    p=patient.objects.get(ID=patID)
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
    return render(request,"patupdatesuccess.html")