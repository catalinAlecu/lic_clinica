from urllib import request
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, CreateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import SignUpForm
from django.contrib.auth.models import User
from .models import Programare, Doctor
from .forms import ProgramareForm
from django.contrib import messages
from django.views.generic import ListView
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
import resend


resend.api_key = settings.RESEND_API_KEY

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

        try:
            resend.Emails.send({
            "from": f"CliniCata <noreply@clinicata.site>",
            "to": [user_email],
            "subject": "Bun venit la CliniCata!",
            "text": f"Bine ai venit, {user_name}\n\nMultumim ca v-ati inregistrat la CliniCata. Suntem incantati sa va avem alaturi!\n\nCu stima,\nEchipa CliniCata"
        })
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
        response = super().form_valid(form)
        
    
        user_email = self.request.user.email
        data_p = form.cleaned_data.get('data_programare')
        specializare = form.cleaned_data.get('specializare')
        nume_doctor = form.cleaned_data.get('doctor')

        subiect = 'Confirmare Programare - CliniCata'
        mesaj = (
            f"Bună {self.request.user.username},\n\n"
            f"Programarea ta a fost înregistrată cu succes!\n"
            f"Doctor: {nume_doctor.nume}\n"
            f"Specializare: {specializare}\n"
            f"Data: {data_p}\n\n"
            f"Mesaj: {form.cleaned_data.get('mesaj')}\n\n"
            f"Te așteptăm cu drag,\nEchipa CliniCata"
        )

        try:
            resend.Emails.send({
                "from": f"CliniCata <noreply@clinicata.site>",
                "to": [user_email],
                "subject": subiect,
                "text": mesaj
            })
        except Exception as e:
            print(f"Eroare la trimitere email programare: {e}")

        return response
    

class ListaProgramariView(LoginRequiredMixin, ListView):
    model = Programare
    template_name = 'lista_programari.html'
    context_object_name = 'programari'

    def get_queryset(self):
        return Programare.objects.filter(pacient=self.request.user).order_by('-data_programare')

class ListaDoctori(ListView):
    model = Doctor
    template_name = 'lista_doctori.html'
    context_object_name = 'doctori'

def doctori_pe_specializare(request):
    specializare_aleasa = request.GET.get('specializare')
    doctori = Doctor.objects.filter(specializare=specializare_aleasa).order_by('nume')
    doctori_list = [{'id': doc.id, 'nume': f"Dr. {doc.nume}"} for doc in doctori]
    return JsonResponse(doctori_list, safe=False)


class AnulareProgramareView(LoginRequiredMixin, DeleteView):
    model = Programare
    success_url = reverse_lazy('lista_programari')

    def get_queryset(self):
        return self.model.objects.filter(pacient=self.request.user)

    def form_valid(self, request, *args, **kwargs):
        programare = self.get_object()
        user_email = self.request.user.email
        
        data_p = programare.data_programare
        specializare = programare.get_specializare_display() if hasattr(programare, 'get_specializare_display') else programare.specializare
        nume_doctor = programare.doctor.nume
        subiect = 'Confirmare Anulare Programare - CliniCata'
        mesaj = (
            f"Bună {self.request.user.username},\n\n"
            f"Programarea ta a fost ANULATĂ cu succes.\n"
            f"Doctor: {nume_doctor}\n"
            f"Specializare: {specializare}\n"
            f"Data: {data_p}\n\n"
            f"Te așteptăm oricând cu o nouă programare,\nEchipa CliniCata"
        )

        try:
            resend.Emails.send({
                "from": f"CliniCata <noreply@clinicata.site>",
                "to": [user_email],
                "subject": subiect,
                "text": mesaj
            })
            messages.success(self.request, "Programarea a fost anulată și emailul de confirmare a fost trimis!")
        except Exception as e:
            print(f"Eroare la trimitere email anulare: {e}")
            messages.warning(self.request, "Programarea a fost ștearsă, dar nu am putut trimite emailul.")

        return super().delete(request, *args, **kwargs)