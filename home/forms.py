from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import (
    ServiceRequest
)

class ServiceRequsetForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['service','name','phone_number','email','description']
        
    
class UserForm(UserCreationForm):
    class Meat:
        model = UserCreationForm
        fields = '__all__'