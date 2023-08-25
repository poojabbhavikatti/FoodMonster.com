from django.shortcuts import render
from bigbasketapp.forms import customer,vendor

from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'index.html')
    
def customer_register(request):
    customer_register = False
    if request.method =='POST':
        userform = customer(request.POST)
        profileform = vendor(request.POST)

        if userform.is_valid() and profileform.is_valid():
           user = userform.save()
           user.set_password(user.password)
           user.save()

           profile = profileform.save(commit=False)
           profile.user = user          #Connecting user model and our own user

           profile.save()
           customer_register = True
    else:
        userform = customer()
        profileform = vendor()
    return render(request,'cregisteration.html',{'userform':userform,'profileform':profileform,'customer_register':customer_register})

def vendor_register(request):
    vendor_register = False
    if request.method =='POST':
        userform = customer(request.POST)
        profileform = vendor(request.POST)

        if userform.is_valid() and profileform.is_valid():
           user = userform.save()
           user.set_password(user.password)
           user.save()

           profile = profileform.save(commit=False)
           profile.user = user          

           profile.save()
           vendor_register = True
    else:
        userform = customer()
        profileform = vendor()
    return render(request,'vregisteration.html',{'userform':userform,'profileform':profileform,'vendor_register':vendor_register})

def base(request):
    return render(request,'base.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('bigbasketapp:base'))
            else:
                return HttpResponse("<h1>User is not active</h1> ")
        else:
            return HttpResponse("<h1>Invalid credentials</h1>")
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('bigbasketapp:index'))