from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:remedio_id>', views.ver_remedio, name='ver_remedio'),
    path('busca', views.busca, name='busca'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)