from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import myUser


# Create your views here.
def index(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pword=request.POST.get('password')
        print(uname,pword)
        try:
            user=get_object_or_404(myUser,username=uname,password=pword)
            print(user,user.logged_in)
            user.logged_in=True
            user.save()
            return redirect(f'/login/{user.username}')
        except:
            return render(request,'login/index.html',{'incorrect':True})
        
    return render(request,'login/index.html',{'incorrect':False})


def dashboard(request,uname):
    if request.method=='POST':
        if request.POST.get('logout')=='yes':
            user=get_object_or_404(myUser,username=uname,logged_in=True)
            user.logged_in=False
            user.save()
            #important
            return redirect('loginIndex')
        else:
            params=['username','password']
            rp=request.POST
            n={}
            
            for p in params:
               n[p]=rp.get(p)
            if (len(myUser.objects.filter(username=n[params[0]]))==0):
                myUser(username=n['username'],password=n['password']).save()
            else:
                users=myUser.objects.all()
        
                return render(request,'login/superuserDash.html',{'name':uname,'users':users,'exist':True})
                
                        
    try:
        user=myUser.objects.get(username=uname,logged_in=True)
        users=myUser.objects.all()
        print('pahuch gya')
        return render(request,'login/superuserDash.html',{'name':uname,'users':users,'exist':False})    
    except myUser.DoesNotExist:
        return redirect('loginIndex')