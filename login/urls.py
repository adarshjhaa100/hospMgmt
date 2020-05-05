from django.urls import path
from . import views

app_name='login'

urlpatterns=[
    path('',views.index,name='loginIndex'),
    path('login/<str:uname>/',views.dashboard,name='superuser'),
    path('login/<str:mainuser>/<str:uname>/update',views.updateUser,name='updateuser'),
    path('login/<str:mainuser>/<str:uname>/delete',views.deleteUser,name='deleteuser')
]