from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, EmergencyContact

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    password1= forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

##create form for emergency contact
class EmergencyContactForm(forms.ModelForm):
    class Meta:
        model = EmergencyContact
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'relationship', 'address', 'city', 'state', 'zip_code', 'country', 'notes']