# Generated by Django 4.0.6 on 2024-06-25 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cartelera', '0004_alter_peliculas_duracion'),
    ]

    operations = [
        migrations.AddField(
            model_name='genero',
            name='portada',
            field=models.FileField(blank=True, null=True, upload_to='generos'),
        ),
        migrations.AddField(
            model_name='peliculas',
            name='portada',
            field=models.FileField(blank=True, null=True, upload_to='portadas'),
        ),
    ]
