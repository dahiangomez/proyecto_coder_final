from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio),

    path("inicio", views.inicio , name="inicio" ),

    path("about", views.about, name="about" ),

    path("profesores" , views.profesores , name="profesores"),
    path("cursos" , views.cursos , name="cursos"),
    path("alumnos" , views.alumnos , name="alumnos" ),

    path("alta_curso" , views.curso_formulario, name='alta_curso'),
    path("alta_profesor" , views.profesor_formulario, name='alta_profesor'),
    path("alta_alumno" , views.alumno_formulario, name='alta_alumno'),

    path("buscar_curso" , views.buscar_curso),
    path("buscar" , views.buscar),

    path("elimina_curso/<int:id>" , views.elimina_curso , name="elimina_curso"),
    path("editar_curso/<int:id>" , views.editar_curso , name="editar_curso"),
    path("editar_curso" , views.editar_curso ,name="editar_curso"),

    path("elimina_alumno/<int:id>" , views.elimina_alumno , name="elimina_alumno"),
    path("editar_alumno/<int:id>" , views.editar_alumno , name="editar_alumno"),
    path("editar_alumno" , views.editar_alumno ,name="editar_alumno"),
    
    path("elimina_profesor/<int:id>" , views.elimina_profesor , name="elimina_profesor"),
    path("editar_profesor/<int:id>" , views.editar_profesor , name="editar_profesor"),
    path("editar_profesor" , views.editar_profesor ,name="editar_profesor"),

    path("login" , views.login_request , name="Login"),
    path("register" , views.register , name="Register"),
    path("logout" , LogoutView.as_view(template_name="logout.html") , name="Logout"),
    path("editarPerfil" , views.editarPerfil , name="editarPerfil")
    
]

