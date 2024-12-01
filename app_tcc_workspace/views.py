from django.shortcuts import render, get_object_or_404, redirect
from .models import TCC
from .forms import TCForm
from django.contrib.auth.decorators import login_required
from .models import TCC, Aluno, Orientador, Curso


# View para exibir os detalhes do TCC
@login_required
def tcc_view(request, tcc_id):
    tcc = get_object_or_404(TCC, id=tcc_id)
    context = {
        'tcc': tcc,
    }
    return render(request, 'tcc.html', context)

# View para editar o TCC (apenas orientador)
@login_required
def tcc_edit(request, tcc_id):
    
    
    tcc = get_object_or_404(TCC, id=tcc_id)
    if request.user != tcc.orientador.user:
        return redirect('tcc', tcc_id=tcc.id)
    
    if request.method == 'POST':
        form = TCForm(request.POST, request.FILES, instance=tcc)
        if form.is_valid():
            form.save()
            return redirect('tcc', tcc_id=tcc.id)
    else:
        form = TCForm(instance=tcc)

    return render(request, 'tcc_edit.html', {'form': form, 'tcc': tcc})

