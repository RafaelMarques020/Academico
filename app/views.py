from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages
from .forms import PessoaForm

class IndexView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all() 
        return render(request, 'index.html', {'pessoas': pessoas})

class PessoasView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoa.html', {'pessoas': pessoas})

class CursosView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        return render(request, 'curso.html', {'cursos': cursos})

class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})

class InstituicoesView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = InstituicaoEnsino.objects.all()
        return render(request, 'instituicao.html', {'instituicoes': instituicoes})

class OcupacoesView(View):
    def get(self, request, *args, **kwargs):
        ocupacoes = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacoes': ocupacoes})

class EditarPessoaView(View):
    template_name = 'pessoa_form.html'
    def get(self, request, id, *args, **kwargs):
        pessoa = get_object_or_404(Pessoa, id=id)
        form = PessoaForm(instance=pessoa)
        return render(request, self.template_name, {'pessoa': pessoa, 'form': form})

    def post(self, request, id, *args, **kwargs):
        pessoa = get_object_or_404(Pessoa, id=id)
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados da pessoa atualizados com sucesso!')
            return redirect('pessoa')
        return render(request, self.template_name, {'pessoa': pessoa, 'form': form})

class DeletePessoaView(View):
    def get(self, request, id, *args, **kwargs):
        pessoa = get_object_or_404(Pessoa, id=id)
        pessoa.delete()
        messages.success(request, 'Registro removido com sucesso!') 
        return redirect('pessoa')

def index(request):
    return render(request, 'index.html')