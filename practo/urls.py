from django.contrib import admin
from django.conf.urls import url
from .views import *
from myadmin.views import *
from clinic.views import *
from covid.views import *
from doctor.views import *
from patient.views import *


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$/', home),
    url(r'home/', home, name='home'),
  #  url(r'adminreg/', adminreg, name='adminreg'),
   # url(r'docreg/', docreg, name='docreg'),
   # url(r'patientreg/', patientreg, name='patientreg'),
   # url(r'covid-19', covid, name='covid'),
   # url(r'clinicreg/', clinicreg, name='clinicreg'),
   # url(r'searchdoc/', searchdoc, name='searchdoc'),
   # url(r'searchclinic/', searchclinic, name='searchclinic'),

]
