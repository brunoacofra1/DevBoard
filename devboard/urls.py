from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', views.teste),
    path('',views.index),
    path('usuario/',include("usuario.urls"))
]
