from django.urls import path

from . import views

urlpatterns = [
    path("api/messages/get", views.GetMessageView.as_view()),
    path("api/messages/send", views.SendMessageView.as_view()),
]