from django.views import View
from django.shortcuts import redirect
from django.http import HttpResponse


class RequiresLoginMixin:
    def dispatch(self, request, *args, **kwargs):
        if "user" not in request.session or request.session["user"] is None:
            redirect_url = getattr(self, "redirect_url", None)
            if redirect_url is not None:
                return redirect(redirect_url)
            handler = getattr(
                self, "not_logged_in", None
            )
            if handler is not None:
                return handler(request)
            return HttpResponse(status=401)
        return super().dispatch(request, *args, **kwargs)
