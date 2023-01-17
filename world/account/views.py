from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from .forms import UserForm, ProfileForm, VerifyForm
from . models import Profile, User
import random
from .helper import MessageHandler
from django.contrib import messages as ms
from django.urls import reverse_lazy
from django.contrib.auth import logout

# Create your views here.

def sign_up(request):
    if request.COOKIES.get('can_otp_enter'):
        return HttpResponseRedirect(reverse_lazy('country:searchdata'))
    else: 
        if request.method == "POST":
            fm=UserForm(request.POST)
            if fm.is_valid():
                fm.save()
                fm=UserForm()
        else:
            fm=UserForm()
        return render(request,"account/signin.html",{'form':fm})

def Log_in(request):
    if request.COOKIES.get('can_otp_enter'):
        return HttpResponseRedirect(reverse_lazy('country:searchdata'))
    else:
        if request.method == "POST":
            if not User.objects.filter(Mobile_number=request.POST['Mobile_number']).exists():
                ms.info(request,"Invalid Mobile number or if you are first time please sign in ")
                return HttpResponseRedirect("/login/")
            if Profile.objects.filter(Mobile_number=request.POST['Mobile_number']):
                ms.info(request,'OTP already sent to this number please check')
                return HttpResponseRedirect("/login/")
            else:     
                getuser = User.objects.get(Mobile_number__iexact=request.POST['Mobile_number'])
                otp=random.randint(1000,9999)
                print(getuser)
                profile=Profile.objects.create(user_id=getuser.email,Mobile_number=request.POST['Mobile_number'],otp=f'{otp}')
                request.session['Mobile_number'] = request.POST['Mobile_number']
                print(request.session['Mobile_number'])
                messagehandler=MessageHandler(request.POST.get('Mobile_number'),otp).send_otp_via_message()
                return redirect(f'otp/{profile.uid}/')
        else:
            fm=ProfileForm()
            return render(request,"account/login.html",{'form':fm})

def otpverify(request,uid):
    if request.method=="POST":
        profile = Profile.objects.get(uid=uid)
        if str(profile) == request.POST['otp']:
            red = HttpResponseRedirect(reverse_lazy('country:searchdata'))
            red.set_cookie("can_otp_enter",True)
            return red
        else:
            ms.info(request,'Wrong OTP.......')
            fm = VerifyForm()
            context ={
                'id':uid,
                'form':fm
            }       
            return render(request,"account/otpverify.html",context)
    fm = VerifyForm()
    context ={
        'id':uid,
        'form':fm
        }       
    return render(request,"account/otpverify.html",context)

def otp_logout(request):
    profile = Profile.objects.get(Mobile_number = request.session.get('Mobile_number'))
    profile.delete()
    if 'Mobile_number' in request.session:
        del request.session['Mobile_number']
    logout(request)
    response = HttpResponseRedirect(reverse_lazy('account:login'))
    response.delete_cookie('can_otp_enter')
    return response