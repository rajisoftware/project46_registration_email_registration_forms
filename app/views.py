from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail 

# Create your views here.
def registration(request):
    ufo=userform()
    pfo=profileform()
    d={'ufo':ufo,'pfo':pfo}
    if request.method=='POST' and request.FILES:
        ufd=userform(request.POST)
        pfd=profileform(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            nsuo=ufd.save(commit=False)
            password=ufd.cleaned_data['password']
            nsuo.set_password(password)
            nsuo.save()
            
            nspo=pfd.save(commit=False)
            nspo.username=nsuo
            nspo.save()
            send_mail('registration',
            "registration is done successfully",
            'dudduguntaraji123@gmail.com',
            [nsuo.email],
            fail_silently=True)

            return HttpResponse('registration is successfull')
        else:
            return HttpResponse('not validate')

    return render(request,'registration.html',d)
