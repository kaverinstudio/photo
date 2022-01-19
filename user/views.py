from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from .forms import SignupForm, UserEditForm
from .models import UserModel


class LoginForm(LoginView):
    template_name = 'layout/default.html'
    form_class = AuthenticationForm


class UserSignupView(FormView):
    template_name = 'user/signup.html'
    form_class = SignupForm

    def form_valid(self, form: SignupForm):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']
        user = UserModel.objects.create_user(username, email, password)
        login(self.request, user)
        return HttpResponseRedirect('/')


class UserEditView(UpdateView):
    form_class = UserEditForm
    model = UserModel

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        user = self.get_object()
        if user != request.user:
            return HttpResponseForbidden('Доступ запрещен')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form: UserEditForm):
        password = form.cleaned_data.get('password1')
        user: UserModel = self.object
        if password:
            user.set_password(password)
            user.save()

        login(self.request, user)
        return HttpResponseRedirect('/')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
