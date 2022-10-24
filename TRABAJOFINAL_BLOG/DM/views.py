from http.client import HTTPResponse
from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CanalMensaje, CanalUsuario, Canal 
from django.http import HttpResponse, Http404
from django.core.exceptions import PermissionDenied


from django.http import HttpResponse

class CanalDetailView(LoginRequiredMixin,DetailView):
    template_name='DM/canal_detail.html'
    queryset = Canal.objects.all()
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_date(*args, **kwargs)
    
        obj = context['object']
        print(obj)
        
        if self.request.user not in obj.usuarios.all():
            raise PermissionDenied
        
    def get_queryset(self):
        usuario= self.request.user
        username=usuario.username
        
        qs=Canal.objects.all().filtrar_por_username(username)
        return qs 

class DetailMs(LoginRequiredMixin,DetailView):
    template_name='DM/canal_detail.html'
    
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
        return HttpResponse("Prohibido")

    mi_username = request.user.username 

    canal, created = Canal.objects.obtener_o_crear_canal_ms(mi_username, username)

    if created:
        print("Si, creado")

        canal, created = canal.canalusuario_set.all().values("usuario__username")

    if created:
        print("Si fue creado!")
    
        Usuario_Canal = canal.canalusuario_set.all(). values("usuario__username")
        print(Usuario_Canal)
        mensaje_canal = canal.canalmensaje_set.all()
        print(mensaje_canal.values("text"))

    return HTTPResponse(f"Nuestro identificador del Canal - {canal.id}")
