from datetime import datetime

from django.core.serializers import serialize
from django.db.models import QuerySet
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import View

from chat_login.mixin import RequiresLoginMixin
from .models import Message


class CSRFExemptMixin:
    @classmethod
    def as_view(cls, **initkwargs):
        return csrf_exempt(super().as_view(**initkwargs))


class GetMessageView(View, RequiresLoginMixin, CSRFExemptMixin):
    redirect_url = "/chat/login/"
    request: HttpRequest

    def post(self, request):
        if "from" not in request.POST:
            return JsonResponse({"messages": [], "error": "invalid shema"})
        from_time = float(request.POST["from"])
        batch_size = request.POST["batch_size"] if "batch_size" in request.POST else 25
        messages: QuerySet = Message.objects
        messages = messages.filter(created_at__range=(datetime.fromtimestamp(from_time), datetime.now()))
        messages: list[Message] = messages.order_by("created_at")[:25]
        return JsonResponse({"messages": serialize("json", messages), "error": ""})

