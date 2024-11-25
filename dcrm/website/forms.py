from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import zoo_user,HotelBooking
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import zoo_user

from .models import zoo_user

# - Register or create a user
class CreateUserForm(UserCreationForm):

    class Meta:
        model = zoo_user
        fields = ['username', 'password1', 'password2']


# - login user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# - add record
class CreationRecordForm(forms.ModelForm):
    class Meta:
        model = zoo_user
        fields = ['first_name', 'last_name', 'email', 'phone', 'address','city']

class UpdateRecordForm(forms.ModelForm):
        class Meta:
            model = zoo_user
            fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city']
class Hotel_Booking_form(forms.ModelForm):

    class Meta:
        model = HotelBooking

        fields = ['hotel_booking_date_arrive', 'hotel_booking_date_leave', 'hotel_booking_adults',
        'hotel_booking_adults', 'hotel_booking_children', 'hotel_booking_oap', 'hotel_total_cost', 'hotel_points']
        labels={
            "hotel_booking_date_arrive": 'day you wish to arrive',
        }
        widgets = {
            'hotel_booking_date_arrive': forms.DateInput(attrs={'type': 'date'}),
            'hotel_booking_date_leave': forms.DateInput(attrs={'type': 'date'}),
            'hotel_total_cost': forms.HiddenInput(),
            'hotel_points': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)