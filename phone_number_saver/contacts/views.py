# contacts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegistrationForm, ContactForm
from .models import Contact 


# Register view
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'contacts/register.html', {'form': form})



def chrome_login(req):
    if 'chrome' in req.session:
        return redirect('contact_list')
    
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['passwd']
        data=authenticate(username=uname,password=password)
        if data:
            if data.is_superuser:
                login(req,data)
                req.session['chrome']=uname   #create session
                return redirect('contact_list')
            else:
                
                login(req,data)
                req.session['user']=uname   
                return redirect('contact_list')
        else:
            messages.warning(req,'Invalid username or password.')
            return redirect(chrome_login)
    else:
        return render(req,'contacts/login.html')



# Login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You are now logged in!")
                return redirect('contact_list')
            else:
                messages.error(request, "Invalid credentials")
    else:
        form = AuthenticationForm()
    return render(request, 'contacts/login.html', {'form': form})

# Logout view
def user_logout(request):
    logout(request)
    messages.success(request, "You have logged out successfully.")
    return redirect('login')

# Contact list view
def contact_list(request):
    if request.user.is_authenticated:
        contacts = Contact.objects.filter(user=request.user)
        return render(request, 'contacts/contact_list.html', {'contacts': contacts})
    else:
        return redirect('login')

# Add contact view
def add_contact(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                contact = form.save(commit=False)
                contact.user = request.user  # Associate contact with logged-in user
                contact.save()
                return redirect('contact_list')
        else:
            form = ContactForm()
        return render(request, 'contacts/add_contact.html', {'form': form})
    else:
        return redirect('login')

