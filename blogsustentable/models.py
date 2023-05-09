from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    cover = models.ImageField(upload_to='images/')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey('blogsustentable.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
    
class Administrador(models.Model):
    Name = models.CharField(max_length=250)
    Rut = models.CharField(primary_key=True,max_length=12)
    Email = models.EmailField('User Mail' ,max_length=250)
    
    
    

class Noticia(models.Model):
    FotoNoticia = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    Titulo = models.TextField(max_length=500)
    Mensaje = models.TextField(max_length=500)
    id = models.TextField(primary_key=True,max_length=12)
    admid = models.ForeignKey(Administrador, on_delete = models.CASCADE)