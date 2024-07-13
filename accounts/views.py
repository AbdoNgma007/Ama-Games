from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import UserProfile

def profile(request):
    if request.user.is_anonymous :
        return redirect("home")
    return render(request, "accounts/profile.html")

def updateProfile(request):
    fname = None
    lname = None
    birthday = None
    nationality = None
    if 'fname' in request.POST: fname = request.POST["fname"]
    if 'lname' in request.POST: lname = request.POST["lname"]
    if 'birthday' in request.POST: birthday = request.POST["birthday"]
    if 'nationality' in request.POST: nationality = request.POST["nationality"]
    if fname and lname and birthday and nationality and "btnupdate" in request.POST:
        user = User.objects.update(first_name=fname, last_name=lname)
        userprofile = UserProfile.objects.get(user=request.user)
        userprofile.birthday=birthday
        userprofile.nationality=nationality
        userprofile.save()
    return redirect("profile")

def logout_view(request):
    auth.logout(request)
    return redirect("home")

def sign_in(request):
    if request.method == "POST" and "btnloging" in request.POST:
        username=request.POST.get("username", None)
        password=request.POST.get("password", None)
        print('=' * 35) 
        if username and password:
            user = auth.authenticate(username=username, password=password)
            print(user)
            if user:
                auth.login(request, user)
                return redirect("home")
    return render(request, "accounts/sign_in.html")

def sign_up(request):
    return render(request, "accounts/sign_up.html")
    
def register_view(request):
    fname = None
    lname = None
    username = None
    password = None
    birthday = None
    nationality = None
    if 'fname' in request.POST: fname = request.POST["fname"]
    if 'lname' in request.POST: lname = request.POST["lname"]
    if 'username' in request.POST: username = request.POST["username"]
    if 'password' in request.POST: password = request.POST["password"]
    if 'birthday' in request.POST: birthday = request.POST["birthday"]
    if 'nationality' in request.POST: nationality = request.POST["nationality"]
    if fname and lname and birthday and nationality and "btnregister" in request.POST and username and password:
        user = User.objects.create_user(first_name=fname, last_name=lname, username=username, password=password)
        user.save()
        userprofile = UserProfile(user=user, birthday=birthday, nationality=nationality)
        userprofile.save()
        user_auth = auth.authenticate(request, username=username, password=password)
        if user_auth is not None:
            auth.login(request, user_auth)
        return redirect("home")
    return render(request, "accounts/sign_up.html")