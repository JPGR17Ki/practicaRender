from django.shortcuts import render, redirect,get_object_or_404
from .models import Genero, Director,Peliculas,Pais,Cine
#importar el sweetalert
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
#Renderiza nuestra página con home.html --> la cual se encuentra en la carpeta de Templates

def home(request):
    return render(request,"home.html")

#GENERO -------------------------------------------------------------------------------- GENERO
 
#Renderizando el Template  de listadoGenero
def listadoGenero(request):
    #Crear un objeto para crear la base de datos y obtener datos
    
    generosBdd = Genero.objects.all()
    return render(request,"listadoGenero.html",
                  {'generos' :generosBdd})

#Renderizando formulario de nuevo genero
def nuevoGenero(request):
   return render(request,'nuevoGenero.html')

#Insertando generos en la base de datos
def guardarGenero(request):
   nom = request.POST["nombre"]
   des = request.POST["descripcion"]
   fot = request.FILES.get("portada")
   nuevoGenero = Genero.objects.create(nombre=nom, descripcion=des, portada=fot)
   messages.success(request,'Genero guardado Exitosamente')
   return redirect('listadoGenero')

#Se recibe el id para eliminar un género
# El primer id = Modelo - id = Parametro
def eliminarGenero(request, id):
    generoeliminar = Genero.objects.get(id=id)
    generoeliminar.delete()
    messages.success(request,'Genero eliminado Exitosamente')
    return redirect('listadoGenero')

#renbderizar el formulario de actualizacion
def editarGenero(request,id):
    generoEditar=Genero.objects.get(id=id)
    return render(request,'editarGenero.html',{'generoEditar':generoEditar})

#actualizar los datos de la BDD
def procesarActualizacionGenero(request):
    id=request.POST['id']
    nom=request.POST['nombre']
    desc=request.POST['descripcion']
    generoConsultado=Genero.objects.get(id=id)
    generoConsultado.nombre=nom
    generoConsultado.descripcion=desc
    generoConsultado.save()
    messages.success(request,'Genero Acutilizado Correctamente.')
    return redirect('listadoGenero')

#PAIS ---------------------------------------------------------------------------------- PAIS
def listadoPais(request):
    #Crear un objeto para crear la base de datos y obtener datos
    paisBdd = Pais.objects.all()
    return render(request,"listadoPais.html",
                  {'paises' :paisBdd})

def nuevoPais(request):
   return render(request,'nuevoPais.html')

def guardarPais(request):
   nom = request.POST["nombre"]
   cont = request.POST["continente"]
   cap = request.POST["capital"]
   nuevoPais = Pais.objects.create(nombre=nom, continente=cont,capital=cap)
   messages.success(request,'Pais guardado Exitosamente')
   return redirect('listadoPais')

def eliminarPais(request, id):
    paiseliminar = Pais.objects.get(id=id)
    paiseliminar.delete()
    messages.success(request,'Pais eliminado Exitosamente')
    return redirect('listadoPais')

def editarPais(request,id):
    paisEditar=Pais.objects.get(id=id)
    return render(request,'editarPais.html',{'paisEditar':paisEditar})

def procesarActualizacionPais(request):
    id=request.POST['id']
    nom = request.POST["nombre"]
    cont = request.POST["continente"]
    cap = request.POST["capital"]
    paisConsultado=Pais.objects.get(id=id)
    paisConsultado.nombre=nom
    paisConsultado.continente=cont
    paisConsultado.capital=cap
    paisConsultado.save()
    messages.success(request,'Pais Acutilizado Correctamente.')
    return redirect('listadoPais')
#DIRECTOR ----------------------------------------------------------------------------------- DIRECTOR

def listadoDirector(request):
    
    #Crear un objeto para crear la base de datos y obtener datos
    
    directorBdd = Director.objects.all()
    return render(request,"listadoDirector.html",
                  {'directores' :directorBdd})

def nuevoDirector(request):
   return render(request,'nuevoDirector.html')

def guardarDirector(request):
   dni = request.POST['dni']
   ape = request.POST["apellido"]
   nom = request.POST["nombre"]
   est = request.POST["estado"]
   fot = request.FILES.get("face")
   nuevoDirector = Director.objects.create(dni=dni, apellido=ape,nombre=nom,estado=est,face=fot)
   messages.success(request,'Director guardado Exitosamente')
   return redirect('listadoDirector')

def eliminarDirector(request, id):
    directoreliminar = Director.objects.get(id=id)
    directoreliminar.delete()
    messages.success(request,'Director eliminado Exitosamente')
    return redirect('listadoDirector')

def editarDirector(request,id):
    directorEditar=Director.objects.get(id=id)
    return render(request,'editarDirector.html',{'directorEditar':directorEditar})

def procesarActualizacionDirector(request):
    id=request.POST['id']
    dni = request.POST['dni']
    ape = request.POST["apellido"]
    nom = request.POST["nombre"]
    est = request.POST["estado"]
    fot = request.FILES.get("face")
    directorConsultado=Director.objects.get(id=id)
    directorConsultado.dni=dni
    directorConsultado.apellido=ape
    directorConsultado.nombre=nom
    directorConsultado.estado=est
    directorConsultado.face=fot
    directorConsultado.save()
    messages.success(request,'Director Acutilizado Correctamente.')
    return redirect('listadoDirector')

#PELICULA ----------------------------------------------------------------------------------- PELICULA

def listadoPelicula(request):
    
    #Crear un objeto para crear la base de datos y obtener datos
    
    peliculaBdd = Peliculas.objects.all()
    return render(request,"listadoPelicula.html",
                  {'peliculas' :peliculaBdd})
    

#cines ----------------------------------------------------------------------------------- cines

def gestionCines(request):
    
    #Crear un objeto para crear la base de datos y obtener datos
    
    cineBdd = Cine.objects.all()
    return render(request,"gestionCines.html",
                  {'cines' :cineBdd})

#Funcion para gestionar el crud de Cines
def gestionCines(request):
    return render(request,'gestionCines.html')

#Insertando cines mediante AJAX en la Base de Datos

@csrf_exempt
def guardarCine(request):
    nom=request.POST["nombre"]
    dir=request.POST["direccion"]
    tel=request.POST["telefono"]
    nuevoCine=Cine.objects.create(nombre=nom,direccion=dir,telefono=tel)    
    return JsonResponse({
        'estado': True,
        'mensaje': 'Género registrado exitosamente.'
    })


#renderizar listados cines
def listadoCines(request):
    cines=Cine.objects.all()
    return render(request, "listadoCines.html", {'cines':cines})


# FETCH -------------------------- PELICULAS

#PELICULA ----------------------------------------------------------------------------------- PELICULA

def nuevaPelicula(request):
    generos = Genero.objects.all()
    directores = Director.objects.all()
    context = {
        'generos': generos,
        'directores': directores,
    }
    return render(request, 'nuevaPelicula.html', context)

@csrf_exempt
def crearPelicula(request):
        titulo = request.POST.get("titulo")
        duracion = request.POST.get("duracion")
        sinopsis = request.POST.get("sinopsis")
        genero_id = request.POST.get("genero")
        director_id = request.POST.get("director")
        portada = request.FILES.get("portada")
        genero = get_object_or_404(Genero, id=genero_id)
        director = get_object_or_404(Director, id=director_id)

        pelicula = Peliculas.objects.create(titulo=titulo, duracion=duracion, sinopsis=sinopsis, genero=genero, director=director,portada=portada)
        
        return JsonResponse({
            'estado': True,
            'mensaje': 'Película registrada exitosamente.'
        })

def listadoPeliculas(request):
    peliculasBdd=Peliculas.objects.all()
    return render(request,"listadoPelicula.html", {'peliculas':peliculasBdd})


#GENERO -------------------------------------------------------------------------------- GENERO


def gestionGenero(request):
    generos = Genero.objects.all()
    return render(request, 'gestionGenero.html', {'generos': generos})

@csrf_exempt
def guardarGenero(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        portada = request.FILES.get('portada')

        nuevoGenero = Genero.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            portada=portada
        )

        return JsonResponse({
            'estado': True,
            'mensaje': 'Género registrado exitosamente.'
        })
    



