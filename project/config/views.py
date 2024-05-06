from django.http import HttpResponse
#from django.template import Context,Template
from django.shortcuts import render
from datetime import datetime


def saludo(request):
    return HttpResponse("Bienvenido al Sitio")

def segunda_vista(request):
    return HttpResponse("<h1>Usando Etiquetas HTML en el responde<h1>")

def nombre(request, nombre, apellido):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"{nombre} {apellido}")


# def probando_template(request):
#     mi_html = open('./template/template1.html', encoding="UTF-8")
#     mi_template = Template(mi_html.read())
#     mi_html.close()
#     mi_contexto = Context()
#     mi_documento = mi_template.render(mi_contexto)
#     return HttpResponse(mi_documento)

def probando_template_render(request):
    nombre = "Oscar"
    apellido = "Farias"
    date = datetime.now()
    datos = {"nombre": nombre, "apellido": apellido, "date": date}
    return render(request, "template1.html", datos)

def mostrar_notas(request):
    notas = (10,3,5,6,9,0,8,7)
    return render(request,"notas.html",{"notas":notas})

def mi_tempalte(request):
    autor = "Oscar Farias"
    return render(request, "new_template.html", {"autor":autor})