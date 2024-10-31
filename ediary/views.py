from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    return render(request, 'home.html')

def help(request):
    return render(request, 'help.html')

def handleLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me', False)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if not remember_me:
                request.session.set_expiry(0)
            return redirect('/diary')
        else:
            messages.error(request,'Username or Password is incorrect')
            return redirect("login")
    else:
        return redirect('error')

def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password']
        password2 = request.POST['password1']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        # Check for validity of the user's information
        try:
            if len(username) < 3 or not username.isalnum(): raise ValueError
            if password1 != password2: raise ValueError
            user = User.objects.create_user(username=username, password=password1, email=email)
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request, "Registration Successful! Please Log in.")
            return redirect('login')
        except ValueError as e:
            messages.error(request, "Username must be longer than 5 characters and alphanumeric")
            return redirect('signup')
    else:
        return render(request, "404.html")

def signin(request):
    if request.user.is_authenticated:
        return redirect('udiary')
    else:
        return render(request, 'login.html')
def signup(request):
    if request.user.is_authenticated:
        return redirect('udiary')
    else:
        return render(request, 'signup.html')
def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully. Thanks for using our service.")
    return redirect("/")

def error(request):
    return render(request, '404.html')

def changePass(request):
    """Change a user's password."""
    if request.method == 'POST':
        oldpass = request.POST['old-password']
        newpass1 = request.POST['new-password']
        newpass2 = request.POST['confirm-password']
        user = request.user
        if user.check_password(oldpass):
            if newpass1 == newpass2:
                user.set_password(newpass1)
                user.save()
                messages.info(request, "Password changed successfully.")
                return redirect('/')
            else:
                messages.warning(request, "New passwords do not match.")
                return redirect('/diary/')
        else:
            messages.warning(request, "Old password is incorrect.")
            return redirect("/diary")        

