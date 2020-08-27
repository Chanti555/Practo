from django.contrib import admin
from django.conf.urls import url
from practo.views import *
from myadmin.views import *
from clinic.views import *
from covid.views import *
from doctor.views import *
from patient.views import *

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$/', home),
    url(r'home/', home, name='home'),

    url(r'adminreg/', adminreg, name='adminreg'),

    url(r'docreg/', docreg, name='docreg'),
    url(r'docregprocess/', docregprocess, name='docregprocess'),
    url(r'docloginform/', docloginform, name='docloginform'),
    url(r'doclogin/', doclogin, name='doclogin'),
    url(r'doceditprocess/', doceditprocess, name='doceditprocess'),
    url(r'docshowform/', docshowform, name='docshowform'),
    url(r'docshowprocess/', docshowprocess, name='docshowprocess'),
    url(r'docupdateform/', docupdateform, name='docupdateform'),
    url(r'docupdate/', docupdate, name='docupdate'),
    url(r'docdeleteform/', docdeleteform, name='docdeleteform'),
    url(r'docdelete/', docdelete, name='docdelete'),
    url(r'dispdoctbyclinic/', dispdocbyclinic, name='dispdoctbyclinic'),
    url(r'dispdoctbyname/', dispdocbyname, name='dispdoctbyname'),
    url(r'displayalldoctors/', displayalldoctors, name='displayalldoctors'),

    url(r'patreg/', patreg, name='patreg'),
    url(r'patregprocess/', patregprocess, name='patregprocess'),
    url(r'patloginform/', patloginform, name='patloginform'),
    url(r'patloginprocess/', patloginprocess, name='patloginprocess'),
    url(r'pateditprocess/', pateditprocess, name='pateditprocess'),
    url(r'patupdateform/', patupdateform, name='patupdateform'),
    url(r'patupdate/', patupdate, name='patupdate'),
    url(r'displayallpatients/', displayallpatients, name='displayallpatients'),
    url(r'patshowform/', patshowform, name='patshowform'),
    url(r'patshowprocess/', patshowprocess, name='patshowprocess'),

    url(r'clinicreg/', clinicreg, name='clinicreg'),
    url(r'clinicregprocess/', clinicregprocess, name='clinicregprocess'),
    url(r'clinicloginform/', clinicloginform, name='clinicloginform'),
    url(r'cliniclogin/', cliniclogin, name='cliniclogin'),
    url(r'cliniceditprocess/', cliniceditprocess, name='cliniceditprocess'),
    url(r'clinicshowform/', clinicshowform, name='clinicshowform'),
    url(r'clinicshowprocess/', clinicshowprocess, name='clinicshowprocess'),
    url(r'clinicupdateform/', clinicupdateform, name='clinicupdateform'),
    url(r'clinicupdate/', clinicupdate, name='clinicupdate'),
    url(r'clinicdeleteform/', clinicdeleteform, name='clinicdeleteform'),
    url(r'clinicdelete/', clinicdelete, name='clinicdelete'),
    url(r'displayallclinics/', displayallclinics, name='displayallclinics'),
    url(r'dispclinicbycity/', dispclinicbycity, name='dispclinicbycity'),


    url(r'covid/', covid, name='covid'),

    url(r'searchdoc/', searchdoc, name='searchdoc'),
    url(r'searchclinic/', searchclinic, name='searchclinic'),

]
