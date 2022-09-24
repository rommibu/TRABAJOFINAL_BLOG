from socket import fromshare
from django.http import HttpResponse
from django.shortcuts import render
from .models import Coberturasalud, Familia, Trabajo, Autos, Post, Category, Comment
from AppMVT.forms import FormularioFamilia, FormularioTrabajo, AutosFormu, UserRegisterForm, AvatarForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
import datetime
#from django.contrib.auth.mixins import loginRequiredMixi
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import*
from django.contrib import messages
from django.views.generic import TemplateView




def inicio(request):
    return render(request, "AppMVT/inicio.html")


def conocenos(request):
    return render(request, "AppMVT/conocenos.html")


def prestadores(request):
    return render(request, "AppMVT/prestadores.html")


def quienes_somos(request):
    return render(request, "AppMVT/quienes_somos.html")


def leyes(request):
    return render(request, "AppMVT/leyes.html")
   
def Cobertura_salud(request):
    # return render(request, "AppMVT/cobertura.html")
    Cobertura1 = Coberturasalud(
        denominacion="Medife", codigo=3624, fecha_creacion="2020-2-20")
    Cobertura1.save()
    Cobertura2 = Coberturasalud(
        denominacion="Swiss Medical", codigo=3782, fecha_creacion="2018-11-22")
    Cobertura2.save()
    Cobertura3 = Coberturasalud(
        denominacion="Pami", codigo=1436, fecha_creacion="2007-5-11")
    Cobertura3.save()
    Cobertura4 = Coberturasalud(
        denominacion="Apross", codigo=41325, fecha_creacion="2022-2-18")
    Cobertura4.save()
    lista = [Cobertura1, Cobertura2, Cobertura3, Cobertura4]
    return render(request, "AppMVT/cobertura.html", {"listado": lista})


def trabajo_titular(request):
    return render(request, "AppMVT/trabajo.html")
    #Trabajo=trabajo(empresa="Tecnofull", antiguedad= 20, profesion="Tecnico", contrato="Propietario")
    # Trabajo.save()
    #texto=f"Descripcion de trabajo agregado: empresa{Trabajo.empresa} antiguedad: {Trabajo.antiguedad} profesion: {Trabajo.profesion} contrato{Trabajo.contrato}"
    # return HttpResponse(texto)


def familia(request):

    if request.method == "POST":
        miFormulario = FormularioFamilia(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            print(info)
            nombre = info.get("nombre")
            apellido = info.get("apellido")
            dni = info.get("dni")
            extranjero = info.get("extranjero")
            enfermedadbase = info.get("enfermedadbase")
            mail = info.get("mail")
            familia = Familia(nombre=nombre, apellido=apellido, dni=dni,extranjero=extranjero, enfermedadbase=enfermedadbase, mail=mail)
            familia.save()
            return render(request, "AppMVT/inicio.html", {"mensaje": "Tu informacion quedo registrada!"})
        else:
            return render(request, "AppMVT/inicio.html", {"mensaje": "Ingreso algun dato incorrecto, por favor verifique!"})
    else:
        miFormulario = FormularioFamilia()
        return render(request, "AppMVT/familia.html", {"formulario": miFormulario})


def formularioTrabajo(request):

    if request.method == "POST":
        form = FormularioTrabajo(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            empresa = info["empresa"]
            antiguedad = info["antiguedad"]
            profesion = info["profesion"]
            contrato = info["contrato"]
            trabajo = Trabajo(empresa=empresa, antiguedad=antiguedad, profesion=profesion, contrato=contrato)
            trabajo.save()
            return render(request, "AppMVT/inicio.html", {"mensaje": "Tu informacion quedo registrada!"})
        else:
            return render(request, "AppMVT/inicio.html", {"mensaje": "Ingreso algun dato incorrecto, por favor verifique!"})
    else:
        form = FormularioTrabajo()
        return render(request, "AppMVT/formularioTrabajo.html", {"formulario": form})

def leerFamilia(request):
    asociados=Familia.objects.all()
    print(asociados)
    return render (request, "AppMVT/leerFamilia.html", {"asociados":asociados})


def busquedaFamilia(request):
    return render(request, "AppMVT/familia.html")

def eliminarAsociado(request, id):
    family=Familia.objects.get(id=id)
    family.delete()
    asociados=Familia.objects.all()
    return render(request, "AppMVT/leerFamilia.html", {"asociados":asociados})


def editarAsociado(request, id):
    family=Familia.objects.get(id=id)
    if request.method=="POST":
        form=FormularioFamilia(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            family.nombre=info["nombre"]
            family.apellido=info["nombre"]
            family.dni=info["dni"]
            family.extranjero=info["extranjero"]
            family.enfermedad=info["enfermedad"]
            family.mail=info["mail"]
            family.save()
            asociados=Familia.objects.all()
            return render(request, "AppMVT/leerFamilia.html", {"asociados":asociados})
    else:
        form=FormularioFamilia(initial={"nombre":family.nombre, "apellido":family.apellido, "dni":family.dni, "extranjero":family.extranjero, "enfermedadbase":family.enfermedadbase, "mail":family.mail, "id":family.id})
        return render(request, "AppMVT/editarAsociado.html", {"formulario":form, "dni_Familia":family.dni})

        

def buscar(request):
    if request.GET["dni"]:
        asociados = request.GET["dni"]
        documentos = Familia.objects.filter(dni=asociados)

        if len(Familia) != 0:
           return render(request, "AppMVT/resultadoBusqueda.html", {"documentos": documentos})
        else:
            return render(request, "AppMVT/resultadoBusqueda.html", {"mensaje": "No se encuentra el dni"})    
    else:
        return render(request, "AppMVT/resultadoBusqueda.html", {"mensaje": "No hay Asociado con este DNI"})
        
     
@login_required
def listar_trabajos(request):
    trabajos = Trabajo.objects.all()
    contexto = {'trabajos':trabajos}
    return render (request, "AppMVT/trabajo.html", contexto)


# Creo la la vista que corresponde a formulario

def escuderia(request):
    if request.method == "POST":
        miFormue = AutosFormu(request.POST)
        print(miFormue)
        if miFormue.is_valid():
            info1 = miFormue.cleaned_data
            print(info1)
            id = info1.get("id")
            nombre = info1["nombre"]
            escuderias = info1["escuderias"]
            piloto = info1["piloto"]
            auto = Autos(id, nombre, escuderias, piloto)
            auto.save()
            return render(request, "AppMVT/inicio.html", {"mensaje": "Exelecente ya estas participando!"})
        else:
            return render(request, "AppMVT/escuderias.html", {"mensaje": "Error"})

    else:
        miFormue = AutosFormu()
        return render(request, "AppMVT/escuderias.html", {"formularioc": miFormue})


def busquedaescu(request):
    return render(request, "AppMVT/resultadoevento.html")



#VISTAS BASADAS EN CLASES

class AsociadoList(ListView):
    model = Familia 
    template_name = 'AppMVT/leerAsociado.html'

class AsociadoDetalle(DetailView):
    model=Familia
    template_name='AppMVT/detalleAsociado.html'



# Buscar info en las tablas.
def Buscar(request):
    if request.GET["nombre"]:

        persona = request.GET["nombre"]
        personas = Autos.objects.filter(nombre=persona)

        if len(personas) != 0:

            return render(request, "AppMVT/busquedaevento.html", {"personas": personas})

        else:
            return render(request, "AppMVT/busquedaevento.html", {"mensaje": "No figurar como registrado, Vamos!! registrate para el evento!!"})
    else:
        return render (request, "AppMVT/resultadoevento.html",{"mensaje": "No figurar como registrado, Vamos!! registrate para el evento!!"})


def login_request(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=request.POST["username"]
            clave=request.POST["password"]

            usuario=authenticate(username=usu, password=clave)

            if usuario is not None:
                login(request, usuario)
                return render(request, 'AppMVT/inicio.html', {'mensaje':f"Bienvenido a Paradigma {usuario}"})
            else:
                return render(request, 'AppMVT/login.html', {"form":form,'mensaje': 'Usuario o contraseña incorrectos'})
        else:
            return render(request, 'AppMVT/login.html', {"form":form,'mensaje': 'Usuario o contraseña incorrectos'}) 
    else:
        form=AuthenticationForm()
        return render(request, 'AppMVT/login.html', {'form':form})


def register(request):
    if request.method=="POST":
        form= UserRegisterForm(request.POST)
        if form.is_valid():
                username=form.cleaned_data["username"]
                form.save()
                return render(request, 'AppMVT/inicio.html', {'mensaje':f"Usuario {username} creado"})
    else:
        form=UserRegisterForm()
        return render(request, 'AppMVT/register.html', {'form':form}) 


@login_request
def agregarAvatar(request):
    if request.method == 'POST':
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if(len(avatarViejo)>0):
                avatarViejo.delete()
            avatar=Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'AppMVT/inicio.html', {'usuario':request.user, 'mensaje':'LISTO TU AVATAR!', "imagen":obtenerAvatar(request)})
    else:
        formulario=AvatarForm()
    return render(request, 'AppMVT/agregarAvatar.html', {'form':formulario, 'usuario':request.user, "imagen":obtenerAvatar(request)})


def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="https://ps.w.org/simple-user-avatar/assets/icon-256x256.png?rev=2413146"
    return imagen



"""def post(request):
   form = Post(request.POST)
   if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=current_user
            post.save()
            messages.success(request, 'Post enviado')
            return redirect ('feed')
    else:
        form = PostForm()
    return render(request, 'AppMVT/post.html.html', {'form':form})


def profile(request):
    return render (request, 'AppMVT/post.html.html')

class BlogHomePageView(TemplateView):
    template_name="blog/inicio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"]= Post.postObjects.all()
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'AppMVT/post-detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.filter(slug=self.kwargs.get('slug'))
        return context"""