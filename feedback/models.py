from django.db import models

class Feedback(models.Model):
    TYPE_CHOICES = [
        ('water', 'Вода'),
        ('gas', 'Газ'),
        ('electricity', 'Электричество'),
    ]

    title = models.CharField(max_length=255, verbose_name="Тема")
    description = models.TextField(verbose_name="Описание")
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name="Тип")
    proposed_solution = models.TextField(blank=True, null=True, verbose_name="Предложение решения")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.type})"

