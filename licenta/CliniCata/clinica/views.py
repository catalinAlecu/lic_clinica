from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class MyLoginView(LoginView):
    template_name = 'login.html'

    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')
