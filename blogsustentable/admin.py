from django.contrib import admin
from .models import Post, Comment
from .models import Administrador

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Administrador)