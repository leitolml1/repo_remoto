from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    titulo=models.CharField(max_length=20)
    contenido=models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    actualizado = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comentarios', on_delete=models.CASCADE)
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    
