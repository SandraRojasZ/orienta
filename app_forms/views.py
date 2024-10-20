from django.shortcuts import render, redirect
from .forms import TCCForm
from django.contrib.auth.decorators import login_required
from .models import TCC

@login_required 
def criar_tcc(request):
    if request.method == 'POST':
        form = TCCForm(request.POST, request.FILES)
        
        if form.is_valid():
           
            print(form.cleaned_data)  
            tcc = form.save(commit=False)
            tcc.orientador = request.user.orientador 
            tcc.save()
            return redirect('dashboard')  
        else:
           
            print(form.errors)  
    else:
        form = TCCForm()
        
    return render(request, 'app_forms/criar_tcc.html', {'form': form})

@login_required
def dashboard(request):
    if hasattr(request.user, 'orientador'):  
        tccs = TCC.objects.filter(orientador=request.user.orientador)
        print(tccs.query)
    else:
        tccs = TCC.objects.filter(autores__user=request.user) 
    # vai direcionar para o templates da app_mentor após a realização do login
    return render(request, 'orientador/pag_mentor.html', {'tccs': tccs}) 
