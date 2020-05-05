from django.urls import path
from . import views

app_name='docmgmnt'

urlpatterns=[
    path('',views.index,name='loginIndex'),
    path('add/',views.addDoctor,name='addDoctor'),
    path('showdoc/',views.showDoc,name='showDoc')
    
]
