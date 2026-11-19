from django.urls import path
from . import views

urlpatterns = [
    path("cars/", views.add_car, name="add_car"),
    path("buy_cars/<int:id>", views.buy_car, name="buy_cars"),
    path("car_details/<int:id>", views.car_details.as_view(), name="car_details"),
    path(
        "purchase/delete/<int:purchase_id>/",
        views.delete_purchase,
        name="delete_purchase",
    ),
    path(
        "comment/delete/<int:id>/", views.delete_comment, name="delete_comment"
    ),
]
