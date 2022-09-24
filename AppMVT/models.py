from tabnanny import verbose
from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from email import contentmanager
#from statistics import mode
#from tkinter import _ExceptionReportingCallback
#from turtle import title
from ckeditor.fields import RichTextField


class  Category(models.Model):
    name=models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset(self).filter(status='published')
    
    options = (
        ('draft', 'Draft'),
        ('published','Published'),
    )
            
    category=models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=255)
    excerpt = models.TextField(null=True)
    content = RichTextField()
    slug =models.SlugField(max_length=250, unique_for_date='published', null=False, unique=True)
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    status = models.CharField(max_length=10, choices=options, default='draft')
    objects= models.Manager()
    postobjectss = PostObjects()

    class Meta:
        ordering = ("-published",)

    def __str__(self):
        return self.title 
    

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Perfil de {self.user.username}'

class Comment (models.Model):
    post= models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name=models.CharField(max_length=50)
    email= models.EmailField()
    content= models.TextField()
    publish= models.DateTimeField(auto_now_add=True)
    status= models.BooleanField(default=True)

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return f"Comment by {self.name}"
 

class Coberturasalud(models.Model):
    denominacion=models.CharField(max_length=60)
    codigo=models.IntegerField()
    fecha_creacion=models.DateField() 

     
#Se modifica de familia a Familia ya que estaba taniendo conflicto
class Familia(models.Model):
    nombre=models.CharField(max_length=60)
    apellido=models.CharField(max_length=60)
    dni=models.FloatField()
    extranjero=models.BooleanField()
    enfermedadbase=models.CharField(max_length=20)
    mail=models.EmailField()

    def __str__ (self):
        return self.apellido+" "+self.nombre

class Trabajo(models.Model):
    empresa=models.CharField(max_length=60)
    antiguedad= models.IntegerField()
    profesion=models.CharField(max_length=50)
    contrato=models.CharField(max_length=60)
    
    def __str__(self) -> str:
        return self.empresa
    
#Agrego el modelo para la eleccion de la escueria, y asi participar por una entrada

class Autos(models.Model):
    nombre = models.CharField(max_length=30)
    
    escuderias= [
        ('Ferrari','Ferrari'),
        ('Mercedes','Mercedes'),
        ('Alpine','Alpine'),
        ('Haas','Haas'),
        ('Alfa Romeo','Alfa Romeo'),
        ('Aston Martin','Aston Martin'),
        ('Alphatauri','Alphatauri'),
        ('Williams','Williams'),
        ('Red Bull','Red Bull'),
        ('Mclaren','Mclaren'),
        
    ]
    
    escuderias = models.CharField(max_length=30,choices=escuderias,default='Ferrari')
    piloto = models.IntegerField()

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares', null=True, blank=True)

#Para el Post
"""class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Perfil de {self.user.username}'
        
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content}'"""
