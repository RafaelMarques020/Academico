"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from app.views import *
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('pessoa/', PessoasView.as_view(), name='pessoa'),
    path('pessoa/editar/<int:id>/', EditarPessoaView.as_view(), name='pessoa_editar'),
    path('pessoa/deletar/<int:id>/', DeletePessoaView.as_view(), name='pessoa_deletar'),
    path('curso/', CursosView.as_view(), name='curso'),
    path('areaSaber/', AreaSaberView.as_view(), name='areaSaber'),
    path('disciplinas/', DisciplinasView.as_view(), name='disciplina'),
    path('matriculas/', MatriculaView.as_view(), name='matricula'),
    path('matriculas/', MatriculaView.as_view(), name='matricula'),
    path('matriculas/', MatriculaView.as_view(), name='matricula'),
    path('turmas/', TurmasView.as_view(), name='turmas'),
    path('avaliacoes/', AvaliacoesView.as_view(), name='avaliacoes'),
    path('frequencias/', FrequenciasView.as_view(), name='frequencias'),
    path('turnos/', TurnosView.as_view(), name='turnos'),
    path('ocorrencias/', OcorrenciasView.as_view(), name='ocorrencias'),
    path('tipos-avaliacao/', TiposAvaliacaoView.as_view(), name='tipos_avaliacao'),
    path('cidade/', CidadesView.as_view(), name='cidade'),
    path('instituicao/', InstituicoesView.as_view(), name='instituicao'),
    path('ocupacao/', OcupacoesView.as_view(), name='ocupacao'),
    path('turmas/', TurmasView.as_view(), name='turmas'),
]

    

