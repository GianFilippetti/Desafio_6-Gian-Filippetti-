from django.shortcuts import render
from django.http import HttpResponse
from desafio.models import familia

# Create your views here.
def modelo (request):
    familia.objects.create (nombre = 'Anto' , edad= 29 , esta_casado =True)
    return HttpResponse ('Aca esta armado mi modelo')

def lista_familiares (request):
    todos_los_familiares = familia.objects.all
    
    context = {
        'familiares': todos_los_familiares
    }
    return render (request ,'lista_familiares.html' , context = context)



