from django.urls import path
from clinica import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
]