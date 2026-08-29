from django.shortcuts import render
from django.http import HttpResponse


def usuario_index(response):
    return HttpResponse("Aqui é o index do usuario")