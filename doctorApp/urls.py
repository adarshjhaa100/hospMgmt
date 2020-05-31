from django.urls import path
from . import views
app_name='docapp'
urlpatterns=[
    path('doclogin/',views.docLogin,name='doclogin'),
    path('<int:id>/',views.index,name='docindex'),
    path('showpatient/<int:id>/<int:did>',views.showPatient,name='showpatient'),
    path('addreport/<int:id>/<int:did>',views.addreport,name='addreport'),

]