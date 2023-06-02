from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    descricao = models.TextField()
    data_criacao = models.DateField()
    website = models.URLField()
    ramo_atuacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Vaga(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='vagas')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    requisitos = models.TextField()
    data_publicacao = models.DateField()
    data_encerramento = models.DateField()
    salario = models.DecimalField(max_digits=8, decimal_places=2)
    tipo_contrato = models.CharField(max_length=100)
    local_trabalho = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo


class Habilidade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    experiencia_profissional = models.TextField()
    educacao = models.TextField()
    vaga_interesse = models.ForeignKey(Vaga, on_delete=models.CASCADE, related_name='candidatos')
    habilidades = models.ManyToManyField(Habilidade)
    curriculo = models.FileField(upload_to='candidatos/curriculos/', null=True, blank=True)

    def __str__(self):
        return self.nome


class Candidatura(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    data_candidatura = models.DateField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"Candidato: {self.candidato} - Vaga: {self.vaga}"