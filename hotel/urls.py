from django.urls import path
from . import views
# Registre suas urls aqui
urlpatterns = [
    path('', views.homepage, name="home"),         # Inclui as urls do app blog

]