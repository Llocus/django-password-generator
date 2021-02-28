from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'Gerador/index.html')

def senha(request):
    caracteres =  list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        caracteres.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('numeros'):
        caracteres.extend(list('0123456789'))
    
    if request.GET.get('especial'):
        caracteres.extend(list('@.-_Çç'))

    tamanho = int(request.GET.get('tamanho',12))

    password = ''

    for x in range(tamanho):
        password += random.choice(caracteres)

    return render(request, 'Gerador/senhas.html', {'senha':password})