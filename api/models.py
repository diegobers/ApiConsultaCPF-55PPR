from django.db import models
 

class CommonMercosulNomenclature(models.Model):
    Codigo = models.CharField(max_length=10, blank=True, primary_key=True)
    Descricao = models.CharField(max_length=5000)
    Data_Inicio = models.CharField(max_length=255)
    Data_Fim = models.CharField(max_length=255)
    Tipo_Ato = models.CharField(max_length=255)
    Numero_Ato = models.CharField(max_length=255)
    Ano_Ato = models.IntegerField()

    def __str__(self):
        return self.Descricao


class ArquivoJSON(models.Model):
    Data_Ultima_Atualizacao_NCM = models.CharField(max_length=255, blank=True, primary_key=True) 
    Nomenclaturas =  models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.Data_Ultima_Atualizacao_NCM

