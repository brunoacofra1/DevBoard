from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns =[
    path('',views.usuario_index,name="index"),
    path('adicionar',views.usuario_adicionar,name="adicionar")
]