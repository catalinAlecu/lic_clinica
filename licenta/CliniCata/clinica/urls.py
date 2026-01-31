from django.urls import path
from django.contrib.auth.views import LogoutView
from clinica import views
from .views import RegisterView, MyLoginView

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('programare/', views.programareView.as_view(), name='programare'),
    path('lista_programari/', views.ListaProgramariView.as_view(), name='lista_programari'),
    path('anulare_programare/<int:pk>/', views.AnulareProgramareView.as_view(), name='anulare_programare'),
]