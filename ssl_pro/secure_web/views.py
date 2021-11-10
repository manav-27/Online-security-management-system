
from django.db.models import query
from django.db.models.base import ModelStateFieldsCacheDescriptor
from django.http.response import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from .models import TT,UserProfile,Guard
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def user_login(request):
    TTm=TT.objects.all
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username , password = password)
        if user is not None:
            login(request, user)
            Gd=Guard.objects.all
            gd=Guard.objects.iterator()
            if user.userprofile.role == 'guard':
                request.session['GG']=username
                
                return render(request,'guard_.html',{'username':username,'TT':TTm,'Guard':Gd})
            else :
                return render(request,'manager_.html',{'username':username,'gd':gd})
        else:
            return HttpResponse("bad creds")

    return render(request,'user_login.html',{})

def user_logout(request):
    logout(request)
    return render(request,'home.html',{})

def holi_req(request):
    
    username=request.session['GG']
    me=Guard.objects.all
    for i in Guard.objects.iterator():
        if i.user.username==username:
            me2=i

    if(me2.AllowedHolidays >= 0):
        salary=15000
    else:
        salary=15000+me2.AllowedHolidays*300

    if request.method == 'POST':
        msg = request.POST['msg']
        datee = request.POST['datee']
        me2.requestmsg=msg
        me2.date=datee
        me2.requestst=1
        me2.save()
        return render(request,'home.html',{})    


    return render(request,'holi_req.html',{'username':username,'me2':me2,'salary':salary})

def holi_app(request):
    if request.method == 'POST':
        username = request.POST['username']
        appden = request.POST['appden']
        msg = request.POST['msg']
        for i in Guard.objects.iterator():
            if i.user.username == username:
                cur=i
        if cur.requestst == 0:
            return HttpResponse("User has no request check properly")


        cur.requestdone=appden
        cur.manno=msg
        cur.requestst=0
        cur.AllowedHolidays-=1
        cur.save()


    
    return render(request,'holi_app.html',{})


"""
def user_regi(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['confirm_password']
        email=None
        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        return HttpResponse(request,"SUCESS")
    
    
    return render(request,'user_regi.html',{})   

"""

               


