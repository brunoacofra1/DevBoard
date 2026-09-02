from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UsuarioForm

def usuario_index(request):
    return render(request, 'usuarios/indexUser.html')

def usuario_adicionar(request:HttpResponse):
    if request.method == "POST":
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("usuarios:index")
    contexto ={
        'formulario':UsuarioForm
    }
    return render(request,'usuarios/adicionarUser.html',contexto)