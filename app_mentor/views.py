from django.shortcuts import render
from projeto_orienta import urls

# Create your views here.
# Função HOME
def home(request):
    return render(request, 'index.html', {'user': request.user})

