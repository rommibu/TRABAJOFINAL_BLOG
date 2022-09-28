from http.client import HTTPResponse
from django.shortcuts import render
from django.views.generic import DetailView
#from django.contrib.auth.mixins import LoginRequiresMixin
from .models import CanalMensaje, CanalUsuario, Canal 
from django.http import HttpResponse, Http404


from django.http import HttpResponse

    

#class DetailMs(LoginRequiresMixin,DetailView):
class DetailMs(DetailView):
    template_name='Dm/canal_detail.html'
    
    def get_object(self, *args, **kwarrgs):
        username = self.kwargs.get("username")
        mi_username = self.request.user.username
        canal, _ = Canal.objects.obtener_o_crear_canal_ms(mi_username, username)

        if username == mi_username:
            mi_canal, _ = Canal.objects.obtener_o_crear_canal_usuario_actual(self.request)

            return mi_canal

        if canal == None:
            raise Http404

        return canal


def mensajes_privados(request, username, *args, **kwargs):

    if not request.user.is_authenticated:
        return HttpResponse("lo siento, No puedes acceder!")

    mi_username = request.user.username

    created = Canal.objects.obtener_o_crear_canal_ms(mi_username, username)

    if created:
        print("Si, creado")

    canal, created = canal.canalusuario_set.all().values("usuario_username")

    if created:
        print("Si fue creado!")
    
        Usuario_Canal = canal.canalusuario_set.all(). values("usuario_username")
        print(Usuario_Canal)
        mensaje_canal = canal.canalmensaje_set.all()
        print(mensaje_canal.values("text"))

    return HTTPResponse(f"Nuestro identificador del Canal - {canal.count()}")
