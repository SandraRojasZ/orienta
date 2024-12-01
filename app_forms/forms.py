from django import forms
from .models import TCC
from app_tcc.models import Aluno

class TCCForm(forms.ModelForm):
    # Campos para os autores
    autor1 = forms.ModelChoiceField(queryset=Aluno.objects.all(), required=False)
    autor2 = forms.ModelChoiceField(queryset=Aluno.objects.all(), required=False)
    autor3 = forms.ModelChoiceField(queryset=Aluno.objects.all(), required=False)

    # Definindo o widget do campo 'data_entrega' para usar o calendário
    data_inicio  = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))    
    data_entrega = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = TCC
        fields = ['titulo', 'descricao','capa', 'autor1', 'autor2', 'autor3', 'curso', 'data_inicio','data_entrega', 'status']
    
    def clean(self):
        cleaned_data = super().clean()
        autor1 = cleaned_data.get('autor1')
        autor2 = cleaned_data.get('autor2')
        autor3 = cleaned_data.get('autor3')

        # Garantir que ao menos um autor seja selecionado
        if not any([autor1, autor2, autor3]):
            raise forms.ValidationError('É necessário adicionar pelo menos um autor.')

        return cleaned_data
