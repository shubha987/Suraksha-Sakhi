from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, EmergencyContactForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import EmergencyContact,User
from .mail import send_email
from .location import lat, log


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page.
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def loginpage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')  # Redirect to a success page.
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

## create contact function
def create_contact(request):
    if request.method == 'POST':
        form = EmergencyContactForm(request.POST)
        if form.is_valid():
            contact=form.save()
            contact.username = request.user.first_name
            contact.save()
            messages.info(request, f"New contact created successfully!!")  # This will save the form data to the database
            return redirect('emergency')  # Redirect to a success page
    else:
        form = EmergencyContactForm()
    return render(request, 'create_contact.html', {'form': form})

def delete_contact(request, id):
    contact = EmergencyContact.objects.get(id=id)
    contact.delete()
    return redirect('emergency')

def update_contact(request, id):
    contact = EmergencyContact.objects.get(id=id)
    form = EmergencyContactForm(instance=contact)
    if request.method == 'POST':
        form = EmergencyContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('emergency')
    return render(request, 'create_contact.html', {'form': form})

def emergency(request):
    contacts = EmergencyContact.objects.all()
    return render(request, 'emergency.html', {'contacts': contacts})

def emergencybutton(request):
    contacts = EmergencyContact.objects.filter(user=request.user)
    link = "http://www.google.com/maps/place/"+lat+","+log
    email=[]
    for contact in contacts:
        email.append(contact.email)
    for contact in contacts:
        send_email(request.user.first_name, email, link)
    return render(request, 'emergencysent.html')

def helpline(request):
    return render(request, 'helpline.html')

def womenlaws(request):
    return render(request, 'womenlaws.html')

def womenrights(request):
    return render(request, 'womenright.html')

@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        if 'emergency' in request.POST:
            return redirect('emergency')
    if request.method == 'POST':
        if 'home' in request.POST:
            return redirect('home')
    return render(request, 'homepage.html')

def logoutpage(request):
    logout(request)
    return redirect('login')
  