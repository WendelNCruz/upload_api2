from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import routers
from uploadapp import views
from uploadapp.api.viewsets import PessoaViewSet, PSexoViewSet

router = routers.DefaultRouter()
router.register(r'Cidade_Meeren', PessoaViewSet, basename='Pessoa')
router.register(r'Classific_Sexo_Idade', PSexoViewSet, basename='PSexo')


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('uploadapp.urls', namespace='uploadapp')),
    path("", views.homepage, name="homepage"),
    path('exportar/', views.export),
    path("upload", views.simple_upload, name="upload"),
    path('api/', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)