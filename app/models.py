from django.db import models
from cpf_field.models import CPFField

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")
    def __str__(self):
        return f"{self.nome}/{self.uf}"
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Ocupação")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome Completo")
    pai = models.CharField(max_length=100, verbose_name="Nome do Pai")
    mae = models.CharField(max_length=100, verbose_name="Nome da Mãe")
    cpf = CPFField(verbose_name="CPF")
    data_nasc = models.DateField(verbose_name="Data de Nascimento")
    email = models.EmailField(verbose_name="E-mail")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name="Ocupação")
    def __str__(self):
        return f"{self.nome}, {self.cpf}, {self.email}, {self.cidade}, {self.ocupacao}"
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Instituição")
    site = models.URLField(verbose_name="Site")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"

class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Área")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Área Saber"
        verbose_name_plural = "Áreas Saber"

class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Curso")
    carga_horaria_total = models.IntegerField(verbose_name="Carga Horária Total")
    duracao_meses = models.IntegerField(verbose_name="Duração (Meses)")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área do Saber")
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Identificação da Turma")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Disciplina")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área do Saber")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

class Turno(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Turno") # Ex: Matutino
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"

class CursoDisciplina(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=50, verbose_name="Período")
    carga_horaria = models.IntegerField(verbose_name="Carga Horária")
    class Meta:
        verbose_name = "Curso/Disciplina"
        verbose_name_plural = "Cursos/Disciplinas"

class Matricula(models.Model):
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()
    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"

class AvaliacaoTipo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Tipo (Prova, Trabalho, etc)")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Avaliação/Tipo"
        verbose_name_plural = "Avaliações/Tipos"

class Avaliacao(models.Model):
    descricao = models.TextField(verbose_name="Descrição da Avaliação")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    tipo = models.ForeignKey(AvaliacaoTipo, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    numero_faltas = models.IntegerField(default=0)
    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"

class Ocorrencia(models.Model):
    descricao = models.TextField()
    data = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Ocorrencia"
        verbose_name_plural = "Ocorrencias"