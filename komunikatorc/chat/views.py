from datetime import datetime

from django.contrib.sessions.backends.db import SessionStore
from django.core.serializers import serialize
from django.db.models import QuerySet
from django.http import JsonResponse, HttpRequest, QueryDict
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import View
from pydantic import BaseModel, ValidationError

from chat_login.mixin import RequiresLoginMixin
from .models import Message, Group, User


class CSRFExemptMixin:
    @classmethod
    def as_view(cls, **initkwargs):
        return csrf_exempt(super().as_view(**initkwargs))


class ParseDataMixin(View):
    class Data(BaseModel):
        pass

    data: Data

    def dispatch(self, request, *args, **kwargs):
        if request.method == "POST":
            try:
                data: QueryDict = request.POST
                self.data = self.Data(**data)
            except ValidationError as e:
                print(f"Bad data, class: {self.__class__!r}", e)
                return JsonResponse({"messages": "", "errors": e.errors()})
        return super().dispatch(request, *args, **kwargs)


APIMixin = (RequiresLoginMixin, CSRFExemptMixin, ParseDataMixin)


class GetLatestMessageView(*APIMixin, View):
    redirect_url = "/chat/login/"
    request: HttpRequest

    class Data(BaseModel):
        group_id: int
        batch_size: int = 25

    def post(self, request):
        messages: QuerySet = Message.objects
        group = Group(id=self.group_id)
        messages = messages.filter(group=group).order_by("-created_at")
        messages: list[Message] = messages[self.data.batch_size:]
        return JsonResponse({"messages": serialize("json", messages), "error": ""})


class GetPreviousMessageView(*APIMixin, View):
    redirect_url = "/chat/login/"
    request: HttpRequest

    class Data(BaseModel):
        group_id: int
        from_time: datetime
        batch_size: int = 25

    def post(self, request):
        messages: QuerySet = Message.objects
        group = Group(id=self.group_id)
        messages = messages.filter(created_at__lt=self.data.from_, group=group)
        messages = messages.order_by("-created_at")
        messages: list[Message] = messages[self.data.batch_size:]
        return JsonResponse({"messages": serialize("json", messages), "error": ""})


class SendMessageView(*APIMixin, View):
    redirect_url = "/chat/login/"
    request: HttpRequest

    class Data(BaseModel):
        group_id: int
        body: str
        reply: int = -1

    def post(self, request):
        group = Group.objects.get(id=self.data.group_id)
        print(group, ", file: chat_login/views.py:81")
        return JsonResponse({"ok"})


class HomeView(RequiresLoginMixin, View):
    def get(self, request):
        user = User.objects.get(id=request.session["user_id"])
        return render(request, "home.html", context={"user": user, "group_id": request.GET.group_id})


def get_session_info(request: HttpRequest):
    session: SessionStore = request.session
    return JsonResponse({"data": {key: session[key] for key in session.keys()}})
