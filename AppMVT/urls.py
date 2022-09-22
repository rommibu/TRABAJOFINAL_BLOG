from django.urls import path
from .views import * 
from django.contrib.auth.views import LogoutView, LoginView 
from django.urls import path, include



urlpatterns = [
    path('', inicio, name='inicio'),
    path('Prestadores/',prestadores, name='prestadores'),
    path('Leyes/', leyes, name='leyes'),
    path('Cobertura/', Cobertura_salud, name='cobertura'),
    path('Trabajos/', listar_trabajos, name='trabajos'),
    path('Conocenos/', conocenos, name='conocenos'),
    path('familia/', familia, name='familia'),
    path('formularioTrabajo/', formularioTrabajo, name='formularioTrabajo'),
    path('busquedaFamilia/', busquedaFamilia, name='busquedaFamilia'),
    path('buscar/', buscar, name='buscar'),
    path('escuderia/',escuderia,name='Eventos'),
    path('Buscar/',Buscar,name='Buscar'),
    path('busquedaescu/',busquedaescu,name='busquedaescu'),
    path('leerFamilia/',leerFamilia,name='leerFamilia'),
    path('eliminarAsociado/<id>', eliminarAsociado, name='eliminarAsociado'),
    path('editarAsociado/<id>', editarAsociado, name='editarAsociado'),
    path('leerFamilia/',leerFamilia,name='leerFamilia'),
    path('post/', Post, name='post'),


   
    #path('familia/list/', FamiliaList.as_view(), name='familia_listar'),
    #path('familia/<pk>', FamiliaList.as_view(), name='familia_detalle'),
    #path('familia/nuevo/', FamiliaList.as_view(), name='familia_crear'),
    #path('familia/editar/<pk>', FamiliaList.as_view(), name='familia_editar'),
    #path('familia/borrar/<pk>', FamiliaList.as_view(), name='familia_borrar'),
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='AppCoder/logout.html), name=logout')),
]