# Generated by Django 5.0.3 on 2024-03-24 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Назва')),
                ('anons', models.CharField(max_length=250, verbose_name='Анонс')),
                ('full_text', models.TextField(verbose_name='Стаття')),
                ('date', models.DateTimeField(verbose_name='Дата публікації')),
            ],
        ),
    ]
