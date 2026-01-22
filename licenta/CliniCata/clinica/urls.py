from django.urls import path
from clinica import views
from .views import RegisterView, MyLoginView

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyLoginView.as_view(), name='login'),
]