from django.shortcuts import render
from django.http import HttpResponse
from desafio.models import familia

# Create your views here.
def modelo (request):
    familia.objects.create (nombre = 'Franco' , edad= 33 , esta_casado = False)
    return HttpResponse ('Aca esta armado mi modelo')

def lista_familiares (request):
    todos_los_familiares = familia.objects.all
    print  (todos_los_familiares)
    context = {
        'familiares': todos_los_familiares
    }
    return render (request ,'lista_familiares.html' , context = context)



