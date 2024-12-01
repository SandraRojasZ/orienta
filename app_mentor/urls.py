from django.urls import path
from . import views  # Certifique-se de importar as views corretamente

urlpatterns = [
    path('index/', views.home, name='index'),
    # Adicione outras URLs do seu app aqui, se necessário
]
