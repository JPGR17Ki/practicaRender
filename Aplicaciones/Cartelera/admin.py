from django.contrib import admin

# Registrar el modelo que creamos

from.models import Genero, Director, Pais, Peliculas
# Register your models here.
admin.site.register(Genero)
admin.site.register(Director)
admin.site.register(Pais)
admin.site.register(Peliculas)
