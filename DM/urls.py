from django.urls import path
from .views import (
    mensajes_privados,
    DetailMs
)


urlpatterns = [
    path('dm/<str:username>', mensajes_privados),
    path('ms/<str:username>', DetailMs.as_view, name='detailms'),
]

