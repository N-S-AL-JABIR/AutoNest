from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import DetailView
from django.http import HttpResponseForbidden


# Create your views here.
def add_car(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = forms.CarForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Car Added Successfully")
                return redirect("add_car")
        else:
            form = forms.CarForm()
        return render(request, "car.html", {"form": form})
    else:
        messages.warning(request, "You Have no access")
        return redirect("profile")


@login_required
def buy_car(request, id):
    car = get_object_or_404(models.Car, id=id)

    if car.quantity > 0:
        models.Purchase.objects.create(user=request.user, car=car)
        car.quantity -= 1
        car.save()
        return redirect("profile")
    else:
        messages.error(request, "This car is out of stock.")
        return redirect("car_list")


@login_required
def delete_purchase(request, purchase_id):
    purchase = get_object_or_404(models.Purchase, id=purchase_id, user=request.user)
    purchase.delete()
    return redirect("profile")


class car_details(DetailView):
    model = models.Car
    pk_url_kwarg = "id"
    template_name = "car_details.html"

    def get_success_url(self):
        return self.request.path

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        comment_form = forms.CommentForm(self.request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = post
            new_comment.user = request.user
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.all()
        context["comment_form"] = forms.CommentForm()
        return context


@login_required
def delete_comment(request, id):
    comment = get_object_or_404(models.Comment, id=id)
    car_id = comment.car.id
    comment.delete()
    return redirect("car_details", id=car_id)
