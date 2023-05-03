from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('post_list.html', views.post_list, name='post_list'),
    path('service1.html', views.service1, name='service1'),
    path('service2.html', views.service2, name='service2'),
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
