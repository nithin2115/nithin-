from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from mini.models import tweet

# Create your views here.
def home(request):
    objs=tweet.objects.all()[::-1]
   
    return render(request,'home.html',{'re':objs})
def loginview(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method=="POST":
        a=request.POST.get('uname')
        b=request.POST.get('passw')
        result=authenticate(request,username=a,password=b)
        if result is not None:
            print(a,b,result)
            login(request,result)   
        else:
            return redirect('loginpage')
    return render(request,'login.html')
def register(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        uname=request.POST.get('uname')
        passw=request.POST.get('passw')
        mail=request.POST.get('mail')
        cpass=request.POST.get('cpass')
        print(fname,lname,uname,passw,mail,cpass)
        if User.objects.filter(username=uname).exists():
            return redirect('loginpage')
            return render(request,'loginpage')
        if len(passw)<8:
            return redirect('registerpage')
        if (passw!=cpass):
            return redirect('registerpage')
        obj=User.objects.create_user(first_name=fname,last_name=lname,email=mail,password=passw,username=uname)
        obj.save()

    return render(request,'register.html')
@login_required(login_url='loginpage')
def profile(request):
    if request.user.is_superuser:
        return redirect('/admin')
    
    return render(request,'profile.html')
def single(request):
    return render(request,'single.html')
@login_required(login_url='loginpage')
def create(request):
    if request.method=="POST":
        a=request.POST.get('p1')
        u=str(request.user.username)
        obj=tweet(uname=u,post=a)
        obj.save()
    return render(request,'create.html')
def displaypage(request,rid):
    b=tweet.objects.get(id=rid)
    if request.method=='POST':
        b.post=request.POST.get('desc')
        b.save()
    return render(request,'display.html',{'res':b})
def logoutview(request):
    logout(request)
   
    return redirect("loginpage")

