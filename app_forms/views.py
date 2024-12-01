from django.shortcuts import render, redirect
from .forms import TCCForm
from django.contrib.auth.decorators import login_required
from app_tcc.models import Aluno
from django.apps import apps

TCC = apps.get_model('app_forms', 'TCC')

@login_required 
def criar_tcc(request):
    if request.method == 'POST':
        form = TCCForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Salva o TCC, mas não salva a relação dos autores ainda
            print(form.cleaned_data) 
            tcc = form.save(commit=False)
            tcc.orientador = request.user.orientador  # Associar o orientador ao TCC
            
            # Associar os autores aos campos autor1, autor2 e autor3
            autor1 = form.cleaned_data.get('autor1')
            autor2 = form.cleaned_data.get('autor2')
            autor3 = form.cleaned_data.get('autor3')
           # Associar os autores ao TCC
            if autor1:
                tcc.autor1 = autor1
            if autor2:
                tcc.autor2 = autor2
            if autor3:
                tcc.autor3 = autor3
            
            tcc.save()  # Salvar as mudanças no banco de dados
            return redirect('dashboard')
        else:
            # Exibe os erros do formulário, se houver
            print("Erros do formulário:", form.errors)
            print("Dados recebidos:", request.POST)
        
    else:
        form = TCCForm()

    alunos = Aluno.objects.all()  # Obtendo todos os alunos para exibir no formulário
    return render(request, 'app_forms/criar_tcc.html', {'form': form, 'alunos': alunos})



@login_required
def dashboard(request):
    if hasattr(request.user, 'orientador'):  
        tccs = TCC.objects.filter(orientador=request.user.orientador)
    else:
        tccs = TCC.objects.filter(autores__user=request.user)
        
    # Gerar string de autores formatada
    for tcc in tccs:
        authors = ', '.join(filter(None, [  
            f"{tcc.autor1.nome} {tcc.autor1.sobrenome}" if tcc.autor1 else '',
            f"{tcc.autor2.nome} {tcc.autor2.sobrenome}" if tcc.autor2 else '',
            f"{tcc.autor3.nome} {tcc.autor3.sobrenome}" if tcc.autor3 else '',
        ]))
        tcc.authors_display = authors  # Atribuir autores formatados
        
    return render(request, 'orientador/pag_mentor.html', {'tccs': tccs})