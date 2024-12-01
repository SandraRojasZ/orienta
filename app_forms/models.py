from django.db import models
from app_tcc.models import Aluno, Orientador, Curso

class TCC(models.Model):
    STATUS_CHOICES = [
        ('em_andamento', 'Em Andamento'),
        ('submetido', 'Submetido'),
        ('aprovado', 'Aprovado'),
        ('reprovado', 'Reprovado'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()    
    capa = models.ImageField(upload_to='capas/')      
    autor1 = models.ForeignKey(Aluno, related_name='tcc_autor1', on_delete=models.CASCADE, null=True, blank=True)
    autor2 = models.ForeignKey(Aluno, related_name='tcc_autor2', on_delete=models.CASCADE, null=True, blank=True)
    autor3 = models.ForeignKey(Aluno, related_name='tcc_autor3', on_delete=models.CASCADE, null=True, blank=True)
         
    orientador = models.ForeignKey(Orientador, on_delete=models.CASCADE)  
    
    data_inicio = models.DateField() 
    data_entrega = models.DateField()
    
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='em_andamento')

    def __str__(self):
        return self.titulo
    
