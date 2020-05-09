from django.urls import path
from . import views
app_name='docapp'
urlpatterns=[
    path('',views.index,name='docindex'),
    path('showpatient/<int:id>/',views.showPatient,name='showpatient'),
    path('addreport/<int:id>/',views.addreport,name='addreport')
]