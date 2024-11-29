from django.shortcuts import render, redirect
from django.contrib.auth import authenticate 
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import ZooUser
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
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, "You have logged in successfully!")
                return redirect('')
            else:
                context = {'register_form':form}
                messages.success(request, "You have logged in successfully!")

                return render(request, 'pages/register.html',context=context)
            
          #  messages.success(request, "You have registered your account successfully!")
          #  return redirect('login')

    context = {'register_form':form}
    return render(request, 'pages/register.html',context=context)

@login_required(login_url='login')
def zooBook(request):
    form = bookZooForm()
    if request.method == "POST":
        updated_request = request.POST.copy()
        updated_request.update({'custID_id':request.user, 'price':'0'})
        form = bookZooForm(updated_request)

        if form.is_valid():
            obj = form.save(commit=False) #Change form into an object instance to be able to manipulate data more easily.

            #pull data from the object to complete calculations
            arrive = obj.dateStart
            depart = obj.dateEnd
            numDays = depart-arrive
            print("Number of Days: ", numDays)

            total_cost = int(obj.adult) * 50\
                        +int(obj.child) * 25
            
            total_cost *= int(numDays.days)
            user_update = request.user
            user_update.points += total_cost//2
            user_update.save()
            print("Hotel Points: ", total_cost//2)
            print("Booking costs", total_cost)

            obj.price = total_cost
            obj.custID = request.user
            obj.save()

            messages.success(request, "Zoo Tickets Booked Successfully!")
            return redirect('')




        else:
            #print out why form is not valid
            print(form.errors)



    
    context = {"zooBookForm":form}
    return render(request, 'pages/bookZoo.html',context=context)

def example(request):
        return render(request, "example/parent.html")
        #order by latest date
        #MyModel.objects.order_by('creation_date').latest()
