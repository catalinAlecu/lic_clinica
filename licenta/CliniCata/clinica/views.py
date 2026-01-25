from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import SignUpForm
from django.core.mail import send_mail 
from django.conf import settings

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

class RegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()

        subject = "Bine ai venit la CliniCata!"
        message = f"Salut {user.username},\n\nÎți mulțumim că te-ai înregistrat la CliniCata. Suntem încântați să te avem alături!\n\nCu stimă,\nEchipa CliniCata"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [user.email]

        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            print("--- EMAIL TRIMIS CU SUCCES! Verifică inbox-ul ---")
        except Exception as e:
            print(f"--- EROARE LA TRIMITERE EMAIL: {e} ---")

            
        return super().form_valid(form)

class MyLoginView(LoginView):
    template_name = 'login.html'

    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')
