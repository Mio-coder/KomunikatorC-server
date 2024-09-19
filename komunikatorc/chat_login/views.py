from django.contrib.auth.hashers import check_password
from django.db.models import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView

from chat.models import User
from chat_login.forms import LoginForm, UserRegistrationForm


class LoginFormView(FormView):
    template_name = "login.html"
    form_class = LoginForm

    def error(self, errors: str, form):
        return render(self.request, "login.html", {"error": errors, "form": form})

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
                return self.error("Invalid password", form)
        else:
            return self.error("User does not exist", form)

    def form_invalid(self, form):
        return self.error(str(form.errors.as_json()), form)


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy("login")  # Redirect after successful registration
