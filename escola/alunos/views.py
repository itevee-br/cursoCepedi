from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Aluno
from .forms import AlunoForm
 
@login_required
def index(request):
    return render(request, 'alunos/index.html')

@login_required
def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/lista_alunos.html', {'alunos': alunos})

@login_required
def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/alunos/')
    else:
        form = AlunoForm()

    return render(request, 'alunos/form_aluno.html', {'form': form})

