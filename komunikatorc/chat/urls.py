from django.urls import path

from . import views

urlpatterns = [
    path("api/messages/", views.GetMessageView.as_view(), name="login")
]