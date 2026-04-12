from django.db import models
from django.contrib.auth.models import User


class Programare(models.Model):
    SPECIALIZARI = [
        ('cardiologie', 'Cardiologie'),
        ('dermatologie', 'Dermatologie'),
        ('pneumologie', 'Pneumologie'),
    ]

    pacient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey('Doctor', on_delete=models.SET_NULL, null=True, blank=True)
    nume_complet = models.CharField(max_length=100)
    telefon = models.CharField(max_length=15)
    specializare = models.CharField(max_length=20, choices=SPECIALIZARI)
    data_programare = models.DateField()
    mesaj = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nume_complet} - {self.data_programare}"
    
class Doctor(models.Model):
    nume = models.CharField(max_length=100)
    specializare = models.CharField(max_length=20, choices=Programare.SPECIALIZARI)
    nume_poza = models.CharField(max_length=100, default='default.jpg')

    def __str__(self):
        return f"Dr. {self.nume}"
