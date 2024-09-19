from datetime import datetime

from django.core.serializers import serialize
from django.db.models import QuerySet
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import View
from msgspec import Struct, field, json, DecodeError

from chat_login.mixin import RequiresLoginMixin
from .models import Message, Group


class CSRFExemptMixin:
    @classmethod
    def as_view(cls, **initkwargs):
        return csrf_exempt(super().as_view(**initkwargs))


class ParseDataMixin(View):
    class Data(Struct):
        pass

    data: Data

    def dispatch(self, request, *args, **kwargs):
        if request.method == "POST":
            try:
                self.data = json.decode(request.POST, type=self.Data)
            except DecodeError as e:
                print(e)
                return JsonResponse({"messages": "", "error": "Invalid data"})
        return super().dispatch(request, *args, **kwargs)


APIMixin = (RequiresLoginMixin, CSRFExemptMixin, ParseDataMixin)


class GetMessageView(*APIMixin, View):
    redirect_url = "/chat/login/"
    request: HttpRequest

    class Data(Struct):
        from_: datetime = field(name="from")
        batch_size: int = field(default=25)

    def post(self, request):
        messages: QuerySet = Message.objects
        messages: list[Message] = messages.filter(created_at__range=(self.data.from_, datetime.now())).order_by("created_at")[:self.data.batch_size]
        return JsonResponse({"messages": serialize("json", messages), "error": ""})


class SendMessageView(*APIMixin, View):
    redirect_url = "/chat/login/"
    request: HttpRequest

    class Data(Struct):
        group_id: int
        body: str
        reply: int = -1

    def post(self, request):
        group = Group.objects.get(id=self.data.group_id)
        print(group)
        return JsonResponse({"ok"})
