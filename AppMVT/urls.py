from django.urls import path
from .views import * 
from . import views
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
    path('eliminarAsociado/<id>', eliminarAsociado, name='eliminarAsociado'),
    path('editarAsociado/<id>', editarAsociado, name='editarAsociado'),
    path('post/', post, name='post'),
    path('leerFamilia/',  leerFamilia, name='leerFamilia'),
    path('', views.feed, name='feed'),
    path('profile/', views.profile, name='profile'),
    
   

   
    path('familia/list/', AsociadoList.as_view(), name='familia_listar'),
    path('familia/<pk>', AsociadoDetalle.as_view(), name='familia_detalle'),
    path('login/', LoginView.as_view(template_name='AppMVT/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='AppMVT/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('editarPerfil/', editarPefil, name='editarPerfil'),
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar'),
    path('<slug:slug>', detallePost, name='detalle_post'),
    
]