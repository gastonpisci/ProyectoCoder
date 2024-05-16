from django.shortcuts import render
from .models import *
from django.http import HttpResponse , HttpRequest
from .forms import CursoFormulario , ProfesorFormulario
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView,UpdateView,CreateView
from django.views.generic.list import ListView



# Create your views here.
def curso(req, nombre, camada):
    curso = Curso(nombre=nombre, camada =camada)
    curso.save()
    
    return HttpResponse(f"""
        <p> Curso: {curso.nombre} - Camada: {curso.camada} agregado! </p>                        
    """)
    
def lista_cursos(req):
    
    lista = Curso.objects.all()
    
    return render(req,"lista_cursos.html",{"lista_cursos": lista} )

def inicio (req)    :
    return render(req,"inicio.html")       

def curso (req)    :
    
    return render(req,"cursos.html")

def profesores (req)    :
    
    return render(req,"profesores.html")

def estudiantes (req)    :
    
    return render(req,"estudiantes.html")

def entregables (req)    :
    estudiante_id = 1
    estudiante = Estudiante.objects.get(id=estudiante_id)
    entregables = Entregable.objects.filter(estudiante=estudiante)
    
    return render(req,"entregables.html" , {"entregables" : entregables})

def curso_formulario (req:HttpRequest)    :
    
    print ('method' , req.method )
    print ('post' , req.POST ) 
    
    if req.method == "POST":        
        
        miFormulario = CursoFormulario(req.POST)
        
        if miFormulario.is_valid():
            print (miFormulario.cleaned_data)
            data =miFormulario.cleaned_data
            
            
            curso = Curso(nombre=data["curso"] , camada =data["camada"])
            curso.save()
            return render(req, "inicio.html",{"mensaje": "Curso creado con exito"})
        else:   
            return render(req, "inicio.html",{"mensaje": "Form invalido"})
            
    else:
        miFormulario = CursoFormulario()
        return render(req,"curso_formulario.html",{"miFormulario" : miFormulario})
    
def busqueda_camada (req)    :
    
    return render(req,"busquedaCamada.html")    


def buscar (req)    :
    
    if req.GET["camada"]:
        camada = req.GET["camada"]
        #curso = Curso.objects.get(camada=camada)
        cursos = Curso.objects.filter(camada__icontains=camada)
        if cursos:
            return render(req,"resultadoBusqueda.html", {"cursos": cursos})  
    else:    
        return HttpResponse('No escribiste bien la camada')
    

def listaProfesores(req):
    
    profesores = Profesor.objects.all()
    
    #contexto= {"profesores":profesores}
    
    return render(req, "leerProfesores.html",{"profesores":profesores})
    
    #return render(req,"busquedaCamada.html")    
    
    
def crea_profesor (req)    :
    

    
    if req.method == "POST":        
        
        miFormulario = ProfesorFormulario(req.POST)
        
        if miFormulario.is_valid():
            
            data =miFormulario.cleaned_data
            
            
            profesor = Profesor(nombre=data["nombre"] , apellido =data["apellido"], email =data["email"], profesion =data["profesion"])
            profesor.save()
            return render(req, "inicio.html",{"mensaje": "Profesor creado con exito"})
        else:   
            return render(req, "inicio.html",{"mensaje": "Form invalido"})
            
    else:
        miFormulario = ProfesorFormulario()
        return render(req,"profesorFormulario.html",{"miFormulario" : miFormulario})  
    
def eliminarProfesor (req, id_profe):

    if req.method == "POST":
        
        eliminaprofe = Profesor.objects.get(id=id_profe)
        eliminaprofe.delete()
        
        profesores = Profesor.objects.all()
    
        #contexto= {"profesores":profesores}
    
        return render(req, "leerProfesores.html",{"profesores":profesores})        
    
def editarProfesor (req,id_profe):
    
    profesor = Profesor.objects.get(id=id_profe)
    
    if req.method == "POST":        
        
        miFormulario = ProfesorFormulario(req.POST)
        
        if miFormulario.is_valid():
            
            data =miFormulario.cleaned_data
            
            profesor.nombre = data["nombre"],
            profesor.apellido = apellido =data["apellido"],
            profesor.email ==data["email"],
            profesor.profesion =  profesion =data["profesion"]            
            
            
            profesor.save()
            return render(req, "inicio.html",{"mensaje": "Profesor editado con exito"})
        else:   
            return render(req, "inicio.html",{"mensaje": "Form invalido"})
            
    else:
        miFormulario = ProfesorFormulario(initial={
            "nombre": profesor.nombre ,
            "apellido" : profesor.apellido,
            "email": profesor.email,
            "profesion": profesor.profesion,           
        })
        
        return render(req,"editarProfesor.html",{"miFormulario" : miFormulario, "id_profe": profesor.id})  
    
    
    
## clase curso list    ()listview


class CursoList(ListView):
    model = Curso
    template_name = "curso_list.html"
    context_object_name = "cursos"
    
class CursoDetail(DetailView):
    model = Curso
    template_name = "curso_detail.html"
    context_object_name = "curso"

class CursoCreate(CreateView):
    model = Curso
    template_name = "curso_create.html"
    fields = ["nombre","camada"]
    success_url = "/app-coder/"
    
class CursoUpdate(UpdateView):
    model = Curso
    template_name = "curso_update.html"
    fields = ["__all__"]
    success_url = "/app-coder/"  
    

class CursoDelete(DeleteView):
    model = Curso
    template_name = "curso_delete.html"
    success_url = "/app-coder/"    


    


# clase curso detail detail view
# class curso create createview
# class cursoUPdate updateview
# class  cursoDElete delteview
    
#crear los html de cada uno de los de arriba. 
# agregar las urls al url.py 

#hay que importar de django.views generic las views
    