from django.urls import path
from cliente.views import index

app_name = "cliente"

urlpatterns = [
    path("", index, name="cliente"),
]