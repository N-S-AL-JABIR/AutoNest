from django.urls import path
from . import views

urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path("profile/edit_profile/", views.edit_profile, name="edit_profile"),
    path("profile/change_pass/", views.pass_change, name="change_pass"),
    path("register/", views.signup, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
]
