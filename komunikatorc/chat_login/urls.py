from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.LoginFormView.as_view(), name="login"),
    path("register/", views.UserRegisterView.as_view(), name="register"),
    path("admin/users/", views.show_users),
]
