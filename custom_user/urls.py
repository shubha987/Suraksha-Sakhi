from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('home/', views.home, name='home'),
    path('home/emergency/', views.emergency, name='emergency'),
    path('home/emergency/create/', views.create_contact, name='create_contact'),
    path('emergencysent/', views.emergencybutton, name='emergencybutton'),
    path('logout/', views.logoutpage, name='logout'),
]