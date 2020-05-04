from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='loginIndex'),
    path('login/<str:uname>/',views.dashboard,name='superuser')
]