from django.shortcuts import render
from brands.models import Brand
from Car.models import Car


def home(request,br_slug=None):
    cars = Car.objects.all()
    if br_slug is not None:
        brands = Brand.objects.get(slug=br_slug)
        cars = Car.objects.filter(brand=brands)
    brands = Brand.objects.all()
    return render(request, "home.html", {"cars": cars, "brands": brands})
