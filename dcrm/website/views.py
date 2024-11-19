from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreationRecordForm, Hotel_Booking_form

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import zoo_user

# Create your views here.



def home(request):
    return render(request, 'website/index.html')

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')

    context = {'form': form}

    return render(request,'website/register.html', context=context)


def my_login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request,data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    
    context = {'login_form':form}
    return render(request,'website/my-login.html', context=context)

def logout(request):
    auth.logout(request)
    return redirect("my-login")

@login_required(login_url='my-login')
def create_record(request):

    form = CreationRecordForm()
    if request.method == "POST":
        form = CreationRecordForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("dashboard")
        
    {'create_form': form}
    return render(request, 'website/create-record.html', context=context)

@login_required(login_url='my-login')
def dashboard(request):

    my_records = zoo_user.objects.all()
    context = {'records': my_records}

    return render(request, 'website/dashboard.html', context=context)

@login_required(login_url='my-login')
def hotel(request):

    form = Hotel_Booking_form()
    
    if request.method =="POST":
        updated_request = request.POST.copy()
        updated_request.update({'hotel_user_id_id': request.user})

        form = Hotel_Booking_form(updated_request)
    
        if form.is_valid():
            obj = form.save(commit=False) #return an object without saving to the DB

            #calculate the number of days
            arrive = obj.hotel_booking_date_arrive
            depart = obj.hotel_booking_date_leave
            result = depart - arrive
            print ("Number of days: ", result.days)


            hotel_total_cost = int(obj.hotel_booking_adults) * 65 \
                                    * int(obj.hotel_booking_children) * 35 \
                                    * int(obj.hotel_booking_oap) * 40
            
            hotel_total_cost *= int(result.days)

            hotel_points = int(hotel_total_cost / 20)
            print("Hotel Points: ", hotel_points)
            print("printing booking costs: ", hotel_total_cost)


            #set the values in the data
            obj.hotel_points = hotel_points
            obj.hotel_total_cost = hotel_total_cost
            obj.hotel_user_id = request.user #add the gotel_user_id field with the user object

            obj.save() #save to database

            messages.success(request, "Hotel booked successfully!")
            return redirect('')
        else:
            print("there was a problem with the form")
            return redirect('hotel')
        
    context = {'form': form}

    return render(request, 'website/hotel.html', context=context)