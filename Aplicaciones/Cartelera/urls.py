#Aplicacion de la Cartelera 


# Configurando redireccionamiento
from django.urls import path

# Importando todas las vistas de Cartelera

from . import views

#Crear un arreglo para llamar al HTML que se creo para listar las bases de datos.

urlpatterns = [
    path('',views.home),
    #--------------------------------------------------   genero 
    path('listadoGenero/',views.listadoGenero, name='listadoGenero'),
    path('nuevoGenero/',views.nuevoGenero, name='nuevoGenero'), #eliminar para el modal
    path('guardarGenero/',views.guardarGenero, name='guardarGenero'),
    path('eliminarGenero/<id>',views.eliminarGenero, name='eliminarGenero'),
    path('editarGenero/<id>',views.editarGenero, name='editarGenero'),
    path('procesarActualizacionGenero/',views.procesarActualizacionGenero, name='procesarActualizacionGenero'),

    #FETCH
    path('gestionGenero/',views.gestionGenero, name='gestionGenero'),
    path('guardarGenero/',views.guardarGenero, name='guardarGenero'),
    

    #--------------------------------------------------   DIRECTOR
    path('listadoDirector/',views.listadoDirector, name='listadoDirector'),
    path('nuevoDirector/',views.nuevoDirector, name='nuevoDirector'),
    path('guardarDirector/',views.guardarDirector, name='guardarDirector'),
    path('eliminarDirector/<id>',views.eliminarDirector, name='eliminarDirector'),
    path('editarDirector/<id>',views.editarDirector, name='editarDirector'),
    path('procesarActualizacionDirector/',views.procesarActualizacionDirector, name='procesarActualizacionDirector'),

    #--------------------------------------------------  PAÍS
    path('listadoPais/',views.listadoPais, name='listadoPais'),
    path('nuevoPais/',views.nuevoPais, name='nuevoPais'),
    path('guardarPais/',views.guardarPais, name='guardarPais'),
    path('eliminarPais/<id>',views.eliminarPais, name='eliminarPais'),
    path('editarPais/<id>',views.editarPais, name='editarPais'),
    path('procesarActualizacionPais/',views.procesarActualizacionPais, name='procesarActualizacionPais'),

    #--------------------------------------------------   PELICULA
    path('listadoPelicula/',views.listadoPelicula, name='listadoPelicula'),
    #FETCH
    path('nuevaPelicula/', views.nuevaPelicula, name='nuevaPelicula'),
    path('crearPelicula/', views.crearPelicula, name='crearPelicula'),

    #--------------------------------------------------   Cine
    path('gestionCines/',views.gestionCines, name='gestionCines'),
    path('guardarCine/',views.guardarCine, name='guardarCine'),
    path('listadoCines/',views.listadoCines, name='listadoCines'),
    
    
    
    
    
    
    
    

]   