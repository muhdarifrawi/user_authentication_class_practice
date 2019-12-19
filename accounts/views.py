from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegistrationForm 
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    return render(request, "accounts/index.template.html")
    
def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect(reverse("index"))
    
def login(request):
    #returns login page
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST["username"], password=request.POST["password"])
            messages.success(request, "You have successfully logged in.")
            
            if user:
                auth.login(user=user, request=request)
                return redirect(reverse("index"))
            else:
                login_form.add_error(None, "Invalid username or password")
                return render(request, "accounts/login.template.html", {
            "form":login_form
        })
    else:
        login_form = UserLoginForm()
        return render(request, "accounts/login.template.html", {
            "form":login_form
        })
     
@login_required
def profile(request):
    User = get_user_model()
    user = User.objects.get(email=request.user.email)
    return render(request, 'accounts/profile.template.html', {
        'user' : user
    })

        
def register(request):
    User = get_user_model()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # do processing
            # after finished processing
            form.save()
            
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            
            if user:
                #if user has been created successfully, attempt to login
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
            else:
                messages.error(request, "Unable to register your account at this time")
            return redirect(reverse('index'))
            
        else:
            return render(request, 'accounts/register.template.html', {
                'form':form
            })
    else:
        
        form = UserRegistrationForm()
        return render(request, 'accounts/register.template.html', {
            'form':form
        })