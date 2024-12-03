from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Contact  # Make sure to import Contact model correctly

# Registration form for creating new user
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Adding an email field

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Form fields for user registration

# Login form for authenticating user
class LoginForm(AuthenticationForm):
    pass  # Using the default AuthenticationForm, no changes necessary

# Contact form for adding new contacts
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact  # Import your Contact model here
        fields = ['name', 'phone_number']  # Fields to create or edit a contact
