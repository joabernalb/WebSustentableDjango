from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as views_auth


urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('noticias.html', views.noticias, name='noticias'),
    path('service1.html', views.service1, name='service1'),
    path('service2.html', views.service2, name='service2'),
    path('service3.html', views.service3, name='service3'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('registrar.html', views.registrar, name='registrar'),
    path('Login/', views_auth.LoginView.as_view(template_name='blog/Login.html'), name='Login'),
    path('Logout/', views_auth.LogoutView.as_view(next_page='index'), name='Logout'),
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
