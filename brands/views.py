from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages

def add_brand(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = forms.BrandForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("brand")
        else:
            form = forms.BrandForm()
        return render(request, "brands.html", {"form": form})
    else:
        messages.warning(request, "You Have no access")
        return redirect("profile")
