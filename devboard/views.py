from django.http import HttpResponse

def teste(request):
    return HttpResponse("Pagina de teste")
def index(request):
    return HttpResponse("<h1>Bem vindo ao DevBoard</h1>")