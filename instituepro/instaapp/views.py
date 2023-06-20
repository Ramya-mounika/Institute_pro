from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import contactData
from .models import Courses
from .models import CommentInfo
import datetime as datetime
import re
from django.contrib import messages

def loginpage(request):
    if request.method=='POST':
        uname=request.POST['uname']
        pass1=request.POST['pass']
        user=authenticate(request,username=uname,password=pass1)
        if user is not None:
            login(request,user)
            return render(request,'mainpage.html')
        else:
            return HttpResponse("username and password are incorrect")
    return render(request,'login.html')

def signuppage(request):
    if request.method=='POST':
        uname=request.POST['uname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        #Check username
        if User.objects.filter(username=uname).exists():
            messages.warning(request,'Username are already exists !')
            return redirect('signup')

        if len(pass1)<8:
            return HttpResponse("length must be 8")
        data=re.findall("[A-Z]{1,}\d{1,}\W{1,}",pass1)
        if data is None:
            return HttpResponse('please enter valid pattern')

        if pass1!=pass2:
            return HttpResponse("your password and conform password are not same")
        else:
            user=User.objects.create_user(username=uname,email=email,password=pass1)
            user.save()
            return redirect('login')

    return render(request,'signuppage.html')

def homepage(request):
    return render(request,'homepage.html')

def contactpage(request):
    if request.method=='GET':
        return render(request,"contactpage.html")
    else:
        contactData(
        firstName=request.POST['fname'],
        lastName=request.POST['lname'],
        mobile=request.POST['mobile'],
        email=request.POST['email'],
        gender=request.POST['gender'],
        course=request.POST['course']
        ).save()
        return redirect("contactpage")

def servicespage(request):
    data=Courses.objects.all()
    return render(request,"servicespage.html",{'nth':data})


def feedbackpage(request):
    if request.method=='GET':
        data=CommentInfo.objects.all().order_by('-rating')
        return render(request,'feedbackpage.html',{'nth':data})
    else:
        CommentInfo(
        content=request.POST['content'],
        rating=request.POST['rate']
        ).save()
        return redirect('feedbackpage')


def deletepage(request,id):
    data=CommentInfo.objects.get(id=id)
    data.delete()
    return redirect("feedbackpage")

def gallerypage(request):
    return render(request,'gallerypage.html')

def mainpage(request):
    return render(request,"mainpage.html")

def logoutpage(request):
    return redirect('loginpage')


def index(request):
    return render(request,'index.html')
