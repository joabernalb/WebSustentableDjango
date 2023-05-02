from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('service1.html', views.service1, name='service1'),
    path('service2.html', views.service2, name='service2'),
    path('service3.html', views.service3, name='service3'),
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)