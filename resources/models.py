from django.db import models

class Resource(models.Model):
    RESOURCE_TYPES = [
        ('water', 'Вода'),
        ('gas', 'Газ'),
        ('electricity', 'Электричество'),
    ]

    STATUS_TYPES = [
        ('available', 'Есть'),
        ('disconnected', 'Отключили'),
        ('soon', 'Скоро отключат'),
    ]

    name = models.CharField(max_length=20, choices=RESOURCE_TYPES)
    status = models.CharField(max_length=20, choices=STATUS_TYPES)
    location = models.CharField(max_length=100)  # например: "ул. Ленина, 5"

    def __str__(self):
        return f"{self.name} - {self.status}"

