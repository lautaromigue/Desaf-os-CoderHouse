from django.shortcuts import render
from familia.models import Familiar

def agregar_familiar(request):
    agregar_familiar = Familiar.objects.create(name='Esteban', age=50, birth = '1972-10-05')
    context = {
        'agregar_familiar':agregar_familiar,
    }
    return render(request, 'agregar_familiar.html', context=context)

def list_familiar(request):
    familiar = Familiar.objects.all()
    context = {
        'familiar':familiar
    }
    return render(request, 'list_familiares.html', context=context)