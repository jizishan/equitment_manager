from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import RegisterForm

class CustomLoginView(LoginView):
    template_name = 'user/login.html'
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    next_page = '/login/'

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'user/register.html'
    success_url = '/login/'