from django.db import models
from django.utils.text import slugify
from brands.models import Brand
from django.contrib.auth.models import User


class Car(models.Model):
    FUEL_TYPE_CHOICES = [
        ("Petrol", "Petrol"),
        ("Diesel", "Diesel"),
        ("Electric", "Electric"),
    ]
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=30)
    fuel_type = models.CharField(max_length=50, choices=FUEL_TYPE_CHOICES)
    engine = models.DecimalField(max_digits=5, decimal_places=1)
    power = models.IntegerField()
    torque = models.IntegerField()
    milage = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100)
    feature_image = models.ImageField(upload_to="uploads/")
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.brand:
            self.slug = slugify(f"{self.brand.name}-{self.model_name}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.brand.name}-{self.model_name}"


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} bought {self.car.model_name}"


class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="comments")
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.car.model_name}"
