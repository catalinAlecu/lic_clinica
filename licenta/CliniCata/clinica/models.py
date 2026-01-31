from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Programare(models.Model):
    SPECIALIZARI = [
        ('cardio', 'Cardiologie'),
        ('derma', 'Dermatologie'),
        ('pneumo', 'Pneumologie'),
    ]

    pacient = models.ForeignKey(User, on_delete=models.CASCADE)
    nume_complet = models.CharField(max_length=100)
    telefon = models.CharField(max_length=15)
    specializare = models.CharField(max_length=20, choices=SPECIALIZARI)
    data_programare = models.DateField()
    mesaj = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nume_complet} - {self.data_programare}"
