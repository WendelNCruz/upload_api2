from django.db import models

CHOICES_GENERO = (
    ('M', 'masculino'),
    ('F', 'feminino'),
)


class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    sobrenome = models.CharField(max_length=128, null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=CHOICES_GENERO)
    altura = models.FloatField(null=True, blank=True, default=None)
    peso = models.FloatField(null=True, blank=True, default=None)
    nascimento = models.DateTimeField(verbose_name="Data Nasc", null=True)
    bairro = models.CharField(max_length=128)
    cidade = models.CharField(max_length=128)
    estado = models.CharField(max_length=64)
    numero = models.DecimalField(max_digits=6, decimal_places=0)

    def __str__(self):
        return self.nome

    def get_nasc(self):
        return self.nascimento.strftime('%d/%m/%Y')
