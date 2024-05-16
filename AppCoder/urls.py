from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [    
    path("agrega-curso/<nombre>/<camada>", curso),  
    path("lista_cursos/", lista_cursos),         
    path("", inicio),
    path("cursos/", curso, name='Cursos'),         
    path("profesores/", profesores,name='Profesores'),         
    path("estudiantes/", estudiantes,name='Estudiantes'),         
    path("entregables/", entregables , name='Entregables'),         
    path("curso-formulario/", curso_formulario , name='CursoFormulario'),         
    path("busqueda-camada/", busqueda_camada , name='BusquedaCamada'),   
    path("buscar/", buscar , name='Buscar'),   
    path("lista-profesores/", listaProfesores , name='ListaProfesores'),
    path("crea-profesor/", crea_profesor , name='CreaProfesor'),
    path("elimina-profesor/<int:id_profe>",eliminarProfesor, name='EliminaProfesores'),
    path("crea-curso/", CursoCreate.as_view() , name='CreaCursos'),
    path("lista-curso/", CursoList.as_view(), name='ListaCursos'),
    path("detalle-curso/<pk>", CursoDetail.as_view() , name='DetalleCursos'),        
    path("actualiza-curso/<pk>", CursoUpdate.as_view() , name='ActualizarCursos'),
    path("elimina-curso/<pk>", CursoDelete.as_view() , name='EliminaCursos'),
]