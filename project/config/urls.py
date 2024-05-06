from django.contrib import admin
from django.urls import path, include
# from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cliente/', include("cliente.urls")),
    path('producto/', include("producto.urls")),
    # path('nombre/<nombre>/<apellido>', views.nombre),
    # path('mihtml', views.probando_template_render),
    # path('notas',views.mostrar_notas),
    # path('mitemplate/', views.mi_tempalte)
]