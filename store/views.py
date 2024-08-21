from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def home(request):
    product = Product.objects.all()
    return render(request, 'home.html',{'products': product})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == "POST":
        username= request.POST['username']
        password= request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, ("You have been Logged in..."))
            return redirect ('home')
        else:
            messages.success(request, ("Username or Password incorrect...Please try again"))
            return redirect ('login')
    else:
        return render( request, 'login.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out...Thank you!'))
    return redirect('home')
