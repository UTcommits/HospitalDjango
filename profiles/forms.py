from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class CreateUserForm(UserCreationForm):
    CHOICES=[('patient','Patient'),('doctor','Doctor'),]
    group = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    class Meta:
        model = User
        fields =['first_name','last_name','username','email','password1','password2',]
    
class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ['user']
    
class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        exclude = ['user']

class PerscriptionForm(ModelForm):
    class Meta:
        model = Perscription
        fields = '__all__'
        widgets = {'doctor': forms.HiddenInput()}
        

class AppointmentForm(ModelForm):
    class Meta:
        model = Appoinments
        fields = '__all__'
        