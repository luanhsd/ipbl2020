from django.db import models
from django.core.validators import MaxValueValidator

class Fornecedor(models.Model):
    cnpj = models.IntegerField(validators=[MaxValueValidator(99999999999)])
    razao_social = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    contato = models.IntegerField(validators=[MaxValueValidator(99999999999)])

    # Função responsavel por pela label do objeto numa lista
    def __str__(self):
        return self.razao_social

class Representante(models.Model):
    cpf = models.IntegerField(validators=[MaxValueValidator(99999999999)])
    nome = models.CharField(max_length=200)
    contato = models.IntegerField(validators=[MaxValueValidator(99999999999)])
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    descricao = models.CharField(max_length=200)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

class Estoque(models.Model):
    descricao = models.CharField(max_length=200)
    quantidade = models.IntegerField(validators=[MaxValueValidator(999999)])

    def __str__(self):
        return self.razao_social


