from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import SignUpForm
from django.contrib.auth.models import User
from .models import Programare
from .forms import ProgramareForm
from django.contrib import messages
from django.views.generic import ListView
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

class RegisterView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object 
        user_email = user.email
        user_name = user.username

        subiect = 'Bun venit la CliniCata!'
        mesaj = f"Bine ai venit, {user_name}\n\nMultumim ca v-ati inregistrat la CliniCata. Suntem incantati sa va avem alaturi!\n\nCu stima,\nEchipa CliniCata"
        expeditor = settings.EMAIL_HOST_USER
        destinatari = [user_email]
        try:
            send_mail(subiect, mesaj, expeditor, destinatari, fail_silently=False)
        except Exception as e:
            print(f"Eroare la trimiterea emailului: {e}")

        return response

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
