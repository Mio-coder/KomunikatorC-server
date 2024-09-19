from django.http import HttpResponse
from django.shortcuts import redirect


class RequiresLoginMixin:
    user_field = "user_id"

    def dispatch(self, request, *args, **kwargs):
        if self.user_field not in request.session or request.session[self.user_field] is None:
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
