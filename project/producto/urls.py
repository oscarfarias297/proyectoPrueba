from django.urls import path
from producto.views import index
app_name = "producto"

urlpatterns = [
    path("", index, name="producto"),
]