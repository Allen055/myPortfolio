from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from home.models import Home

# Create your views here.

def profile(request):
    home = Home.objects.first()
    return render(
        request,
        "accounts/profile.html",
        {
            "home": home
        }
   )


def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            login(request, form.get_user())
            return redirect("dashboard:dashboard")

    return render(request, "accounts/login.html", {"form": form})


def activate(request, uid):
    user = get_object_or_404(User, pk=uid)

    user.is_active = True
    user.save()

    profile = user.userprofile
    profile.email_verified = True
    profile.save()

    messages.success(request, "Your email has been verified. You can now log in.")

    return redirect("accounts:login")



def logout_view(request):
    logout(request)
    return redirect("accounts:login")