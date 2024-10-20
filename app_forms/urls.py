from django.urls import path
from .views import criar_tcc, dashboard  

urlpatterns = [
    path('criar_tcc/', criar_tcc, name='criar_tcc'),
    path('dashboard/', dashboard, name='dashboard'),  
]

