from django.shortcuts import render
from django.http import HttpResponse

def usuario_index(request):
    return render(request, 'usuarios/indexUser.html')
def usuario_adicionar(request):
    return render(request,'usuarios/adicionarUser.html')