from django.test import TestCase

from .models import Canal, CanalUsuario, CanalMensaje,

from django.contrib.auth import get_user_model

User=get_user_model()


class CanalTestCase(TestCase):
    def setUp(self):
        self.usuario_a = User.objects.create(username='Romi', password='Romi4899')
        self.usuario_a = User.objects.create(username='Romina', password='bien')
        self.usuario_a = User.objects.create(username='PEPITO', password='Python25')

    def test_usuario_count(self):
        qs=User.objects.all()
        self.assertEqual(qs.count(),3) #funcion para verificar si 2 variables son iguales
    
    def test_cada_usuario_canal(self):
        qs=User.objects.all()
        for usuario in qs:
            canal_obj = Canal.objects.create()
            canal_obj.usuarios.add(usuario)

            canal_qs=Canal.objects.all()
            self.assertEqual(canal_qs.count(),3)
            canal_qs_1=canal_qs.solo_uno()
            self.assertEqual(canal_qs.count(),canal_qs.count())

    def prueba_dos_usuarios(self):
        canal_obj = Canal.objects.create()
        CanalUsuario.objects.create(usuario=self.usuario_a, canal=canal_obj)
        CanalUsuario.objects.create(usuario=self.usuario_b, canal=canal_obj)

        canal_obj2 = Canal.objects.create()
        CanalUsuario.objects.create(usuario=self.usuario_c, canal=canal_obj2)
        
        qs=Canal.objects.all()
        self.assertEqual(qs.count(),2)
        solo_dos = qs.solo_dos()
        self.assertEqual(solo_dos.count(),1)