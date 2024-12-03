# contacts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),  
    path('add/', views.add_contact, name='add_contact'),  
    path('register/', views.register, name='register'),  
    path('contacts/login/', views.user_login, name='login'),  
    path('logout/', views.user_logout, name='logout'), 
]


