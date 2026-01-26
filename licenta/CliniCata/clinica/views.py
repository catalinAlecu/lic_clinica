from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from .models import Programare
from .forms import ProgramareForm
from django.contrib import messages
from django.views.generic import ListView

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
    
class programareView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = ProgramareForm
    template_name = 'programare.html'
    success_url = reverse_lazy('home')
    success_message = "Programarea a fost realizata cu succes!"
    login_url = 'login'

    def get_initial(self):
        initial = super().get_initial()
        initial['nume_complet'] = f"{self.request.user.first_name} {self.request.user.last_name}"
        return initial

    def form_valid(self, form):
        form.instance.pacient = self.request.user
        return super().form_valid(form)
    

class ListaProgramariView(LoginRequiredMixin, ListView):
    model = Programare
    template_name = 'lista_programari.html'
    context_object_name = 'programari'

    def get_queryset(self):
        return Programare.objects.filter(pacient=self.request.user).order_by('-data_programare')
