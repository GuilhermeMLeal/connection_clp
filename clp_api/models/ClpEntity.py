from django.db import models

# Create your models here.
class ClpInformation(models.Model):
    Sensor = models.BooleanField(default=False)
    Botao = models.BooleanField(default=False)
    LigaRobo = models.BooleanField(default=False)
    ResetContador = models.BooleanField(default=False)
    ValorContagem = models.IntegerField(default=0)

    def __str__(self):
        return f"Configuração - Sensor: {self.Sensor}, Botão: {self.Botao}, Liga Robô: {self.LigaRobo}, Reset Contador: {self.ResetContador}, Valor Contagem: {self.Valor_Contagem}"