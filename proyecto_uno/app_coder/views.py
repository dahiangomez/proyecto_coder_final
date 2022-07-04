from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Curso
from app_coder.models import Alumno
from app_coder.models import Profesor
from app_coder.models import Avatar
from django.template import loader
from app_coder.forms import Curso_formulario
from app_coder.forms import Alumno_formulario
from app_coder.forms import Profesor_formulario
from app_coder.forms import UserEditForm
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required 


def inicio(request):
    
    return render( request , "inicio.html" )

def about(request):
    
    return render( request , "about.html" )

def cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos" : cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento )

def alumnos(request):
    alumnos = Alumno.objects.all()
    dicc = {"alumnos" : alumnos}
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento )
 
def profesores(request):
    profesores = Profesor.objects.all()
    dicc = {"profesores" : profesores}
    plantilla = loader.get_template("profesores.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento )  



def curso_formulario(request):

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            curso = Curso( nombre=datos['nombre'] , camada=datos['camada'] )
            curso.save()

            return render( request , "alta_curso.html")

    return render( request, "alta_curso.html")

def alumno_formulario(request):

    if request.method == "POST":

        mi_formulario = Alumno_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            alumno = Alumno( nombre=datos['nombre'] , camada=datos['camada'] , nacimiento=datos['nacimiento'] )
            alumno.save()

            return render( request , "alta_alumno.html")

    return render( request, "alta_alumno.html")

def profesor_formulario(request):

    if request.method == "POST":

        mi_formulario = Profesor_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            profesor = Profesor( nombre=datos['nombre'] , camada=datos['camada']  , nacimiento=datos['nacimiento'] )
            profesor.save()

            return render( request , "alta_profesor.html")

    return render( request, "alta_profesor.html")


def buscar_curso(request):

    return render( request , "buscar_curso.html")



def buscar(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']      
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busqueda.html" , {"cursos": cursos})
    else:
        return HttpResponse("Campo vacio")
   


@login_required
def elimina_curso( request , id):

    curso = Curso.objects.get(id=id)
    curso.delete()

    curso = Curso.objects.all()

    return render(request , "cursos.html" , {"cursos": curso})



@login_required
def editar_curso( request , id):

    curso = Curso.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos['nombre']
            curso.camada = datos['camada']
            curso.save()

            curso = Curso.objects.all()          
            return render(request , "cursos.html" , {"cursos": curso})
    else:
        mi_formulario = Curso_formulario(initial={'nombre':curso.nombre , "camada":curso.camada})
    
    return render( request , "editar_curso.html" , {"mi_formulario":mi_formulario, "curso": curso})


@login_required
def elimina_alumno( request , id):

    alumno = Alumno.objects.get(id=id)
    alumno.delete()

    alumno = Alumno.objects.all()

    return render(request , "alumnos.html" , {"alumnos": alumno})



@login_required
def editar_alumno( request , id):

    alumno = Alumno.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Alumno_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno.nombre = datos['nombre']
            alumno.camada = datos['camada']
            alumno.nacimiento = datos['nacimiento']
            alumno.save()

            alumno = Alumno.objects.all()          
            return render(request , "alumnos.html" , {"alumnos": alumno})
    else:
        mi_formulario = Alumno_formulario(initial={'nombre':alumno.nombre , "camada":alumno.camada, 'nacimiento':alumno.nacimiento})
    
    return render( request , "editar_alumno.html" , {"mi_formulario":mi_formulario, "alumno": alumno})



@login_required
def elimina_profesor( request , id):

    profesor = Profesor.objects.get(id=id)
    profesor.delete()

    profesor = Profesor.objects.all()

    return render(request , "profesores.html" , {"profesores": profesor})



@login_required
def editar_profesor( request , id):

    profesor = Profesor.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Profesor_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor.nombre = datos['nombre']
            profesor.camada = datos['camada']
            profesor.nacimiento = datos['nacimiento']
            profesor.save()

            profesor = Profesor.objects.all()          
            return render(request , "profesores.html" , {"profesores": profesor})
    else:
        mi_formulario = Profesor_formulario(initial={'nombre':profesor.nombre , "camada":profesor.camada, 'nacimiento':profesor.nacimiento})
    
    return render( request , "editar_profesor.html" , {"mi_formulario":mi_formulario, "profesor": profesor})



def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request , data= request.POST)

        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contra)

            if user is not None:
                login(request,user)
                avatares = Avatar.objects.filter(user=request.user.id)
                return render( request , "inicio.html" ,{"url":avatares[0].imagen.url} )
                
    
            else:
                return HttpResponse(f"Usuario Incorrecto")
        else:         
            return HttpResponse(f"FORM INCORRECTO {form}")

    form = AuthenticationForm()

    return render( request , "login.html" , {"form":form})



def register(request):

    if request.method == "POST":
        
        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()
            return HttpResponse("Usuario creado")

    else:
        form = UserCreationForm()
    return render( request , "registro.html" , {"form":form})



@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == "POST":
        
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            password = informacion['password1']
            usuario.set_password(password)
            usuario.save()

            return render( request , "inicio.html")

    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render( request , "editar_perfil.html" , {"miFormulario":miFormulario , "usuario":usuario})


