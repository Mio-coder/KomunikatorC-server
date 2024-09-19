from django.urls import path

from . import views

urlpatterns = [
    path("home/<group_id:int>", views.HomeView.as_view()),
    path("api/messages/latest/", views.GetLatestMessageView.as_view()),
    path("api/messages/previous/", views.GetPreviousMessageView.as_view()),
    path("api/messages/send/", views.SendMessageView.as_view()),
    path("admin/session/", views.get_session_info),
]
