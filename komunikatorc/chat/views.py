from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import render
from .forms import LoginForm, SignUpForm
import json


def login(request: HttpRequest) -> JsonResponse | HttpResponse:
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


def signup(request: HttpRequest) -> JsonResponse | HttpResponse:
    if request.method == "POST":
        # api
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            confirm_password = form.cleaned_data["confirm_password"]
            if password != confirm_password:
                return JsonResponse({"errors": form.errors.as_json()}, status=400)
            return JsonResponse({"session_id": "absb-hrqp-foae-tyui"}, status=200)
        else:
            return JsonResponse({"errors": form.errors.as_json()}, status=400)
    form = SignUpForm()
    return render(request, "signup.html", {"form": form})
