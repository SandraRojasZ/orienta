from django.urls import path
from . import views

urlpatterns = [
    path('tcc/<int:tcc_id>/', views.tcc_view, name='tcc'),
    path('tcc/<int:tcc_id>/edit/', views.tcc_edit, name='tcc_edit'),
]
