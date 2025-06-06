# Generated by Django 5.1.3 on 2025-05-25 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('water', 'Вода'), ('gas', 'Газ'), ('electricity', 'Электричество')], max_length=20)),
                ('status', models.CharField(choices=[('available', 'Есть'), ('disconnected', 'Отключили'), ('soon', 'Скоро отключат')], max_length=20)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
