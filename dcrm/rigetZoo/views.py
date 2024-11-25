from django.shortcuts import render, redirect
from django.contrib.auth import authenticate 
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import LoginForm, CreateUserForm, bookZooForm

# Create your views here.
def home(request):
    webpage = 'pages/index.html'
    context={'bgImage': 'tiger.jpg',}
    return render(request, webpage, context=context)

def visitUs(request):
    webpage = 'pages/visitUs.html'
    context={'bgImage': 'parrot.jpg',}
    return render(request, webpage, context=context)

def visitEdu(request):
    webpage = 'pages/visitEdu.html'
    context={'bgImage': 'schoolVisit.jpg',}
    return render(request, webpage, context=context)

def whatsHere(request):
    webpage = 'pages/whatsHere.html'
    context={'bgImage': 'parkEntrance.jpg',}
    return render(request, webpage, context=context)

def aboutUs(request):
    webpage = 'pages/aboutUs.html'
    context={'bgImage': 'teamphoto.jpg',}
    return render(request, webpage, context=context)

def login(request):
    return redirect()

#logout user
def user_logout(request):
    auth.logout(request)
    messages.success(request, "You have logged out successfully!")
    return redirect("login")

def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, "You have logged in successfully!")
                return redirect('')

    context = {'login_form':form}
    return render(request, 'pages/login.html',context=context)


# def payScreen(request):
#     booking = Hotel_Booking.objects.latest("customer_id")
#     context = {'paymentForm': form,
#                 'booking':booking}


#     form = booking_form()
#     if request.method == "POST":
#         if form in method.POST:


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have registered your account successfully!")
            return redirect('login')

    context = {'register_form':form}
    return render(request, 'pages/register.html',context=context)

def zooBook(request):
    form = bookZooForm()
    context = {"zooBookForm":form}
    return render(request, 'pages/bookZoo.html',context=context)

def example(request):
        return render(request, "example/parent.html")
