from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('service1.html', views.service, name='Service1'),
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)