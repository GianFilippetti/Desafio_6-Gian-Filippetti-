from django.http import HttpResponse
from django.shortcuts import render



def familiares (request):
    context = {
        'Familiares' : ['Matilde Fagonde', 'Miguel Filippetti', 'Anto Filippetti' , 'Franco Filippetti', 'Pinitus']
    }
    return render (request ,'familiares.html' , context = context )