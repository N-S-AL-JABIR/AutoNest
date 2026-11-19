from django.shortcuts import render, redirect
from . import forms
from Car.models import Purchase
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = forms.UserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Account Created Successfully")
                return redirect("profile")
        else:
            form = forms.UserForm()
        return render(request, "register.html", {"form": form, "type": "Register"})
    else:
        return redirect("home")


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                messages.success(request, "Logged in Successfully")
                return redirect("home")
            else:
                messages.warning(request, "Login information is incorrect.")
        else:
            form = AuthenticationForm()
        return render(request, "register.html", {"form": form, "type": "Login"})
    else:
        return redirect("home")


@login_required
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("login")


@login_required
def profile(request):
    user = request.user
    purchases = Purchase.objects.filter(user=request.user)
    return render(request, "profile.html", {"user": user, "purchases": purchases})


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = forms.ChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Updated Successfully")
            return redirect("profile")
    else:
        form = forms.ChangeForm(instance=request.user)
    return render(request, "register.html", {"form": form, "type": "Edit Profile"})


@login_required
def pass_change(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password updated Successfully")
            return redirect("profile")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "register.html", {"form": form, "type": "Change Password"})
