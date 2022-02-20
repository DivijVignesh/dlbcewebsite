from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views


from . import views
from . import profileview
urlpatterns = [    
    path('', views.mainhome, name='home'),
    path('secretary', views.secretary, name='secretary'),
    path('profile', views.profile, name='profile'),
    path('principal', views.principal, name='principal'),
    path('contact', views.contact, name='contact'),
    
    path('cse/home', views.csehome, name='csehome'),
    path('cse/profile', views.cseprofile, name='cseprofile'),
    path('cse/hod', views.csehod, name='csehod'),
    path('cse/faculty/<str:name>/',profileview.profileview, name='profilecsetemplate'),
    path('cse/faculty', views.csefaculty, name='csefaculty'),
    path('cse/activities', views.cseactivities, name='cseactivities'),
    
    
    path('civil/home', views.civilhome, name='civilhome'),
    path('civil/profile', views.civilprofile, name='civilprofile'),
    path('civil/faculty', views.civilfaculty, name='civilfaculty'),
    path('civil/hod', views.civilhod, name='civilhod'),
    path('civil/activities', views.civilactivities, name='civilactivities'),
    path('civil/faculty/<str:name>/',profileview.profileview, name='profileciviltemplate'),

    
    path('eee/faculty', views.eeefaculty, name='eeefaculty'),
    path('eee/home', views.eeehome, name='eeehome'),
    path('eee/profile', views.eeeprofile, name='eeeprofile'),
    path('eee/hod', views.eeehod, name='eeehod'),
    path('eee/activities', views.eeeactivities, name='eeeactivities'),
    path('eee/faculty/<str:name>/', profileview.profileview, name='profileeeetemplate'),
    
    
    path('ece/home', views.ecehome, name='ecehome'),
    path('ece/faculty', views.ecefaculty, name='ecefaculty'),
    path('ece/profile', views.eceprofile, name='eceprofile'),
    path('ece/hod', views.ecehod, name='ecehod'),
    path('ece/activities', views.eceactivities, name='eceactivities'),
    path('ece/faculty/<str:name>/', profileview.profileview, name='profileecetemplate'),
    
    
    path('bs/faculty', views.bsfaculty, name='bsfaculty'),
    path('bs/home', views.bshome, name='bshome'),
    path('bs/profile', views.bsprofile, name='bsprofile'),
    path('bs/hod', views.bshod, name='bshod'),
    path('bs/activities', views.bsfaculty, name='bsactivities'),
    path('bs/faculty/<str:name>/', profileview.profileview, name='profilebstemplate'),


    
    
]