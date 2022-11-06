from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
import templates
import email_verification.code_files.sent_mail_file as data
from django.shortcuts import redirect

# Create your views here.
emailid=""

def home(request):
    global data1,emailid
    if request.method =="POST":
        email=request.POST.get("inputEmail")
        request.session['email']=email
        gen_password_sent_mail=data.create_mail(email)
        print(gen_password_sent_mail)
        emailid=email
        data1=gen_password_sent_mail
        if(data1):
            return HttpResponseRedirect('verify')
    return render(request,'index.html')

def verify(request):
    if (emailid and "email" in request.session):
        if request.method =="POST":
            password_by_user=request.POST.get("inputPassword")
            if(password_by_user==data1):
                return HttpResponseRedirect('dashboard')
            else:
                message='Wrong OTP entered Kindly check and try again.'
                return render(request,'verify.html', {'message':message})
        return render(request,'verify.html')
    else:
        return HttpResponseRedirect('/')

def dashboard(request):
    if "email" in request.session:
        session_email=request.session['email']
        print(session_email )
        return render(request,'Dashboard.html',{'session_email':session_email})
    else:
        return HttpResponseRedirect('/')

def logout_fun(request):
    del request.session['email']
    print("Inside views function")
    return HttpResponseRedirect('/')