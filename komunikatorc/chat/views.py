from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from .forms import LoginForm


def login(request: HttpRequest):
    if request.method == "POST":
        # api
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            return JsonResponse({"session_id": "absb-hrqp-foae-tyui"}, status=200)
        else:
            return JsonResponse({"errors": form.errors.as_json()}, status=400)
    form = LoginForm()
    return render(request, "login.html", {"form": form})
