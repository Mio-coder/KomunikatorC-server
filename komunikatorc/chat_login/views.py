from django.contrib.auth.hashers import check_password
from django.db.models import QuerySet
from django.http import JsonResponse, HttpRequest
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.shortcuts import redirect, render

from chat.models import User
from chat_login.forms import LoginForm, UserRegistrationForm


class LoginFormView(FormView):
    template_name = "login.html"
    form_class = LoginForm

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]

        # Check if the user exists
        users: QuerySet = User.objects.filter(username=username)
        print(users)
        if users.exists():
            user: User = users.get()
            print(f"{user.username=} {user.password=}")
            # Verify the password
            if check_password(password, user.password):
                # Store session data
                self.request.session['user_id'] = user.id
                return redirect("/chat/home/")
            else:
                return render(self.request, "login.html", {"error": "Invalid password"})
        else:
            return render(self.request, "login.html", {"error": "User does not exist"})

    def form_invalid(self, form):
        return JsonResponse({"errors": form.errors.as_json()}, status=400)


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy("login")  # Redirect after successful registration


def show_users(request: HttpRequest):
    x: QuerySet = User.objects
    return JsonResponse([["username", "password"]] + [[u.username, u.password] for u in x.all()], safe=False)
