from django.db import models
 
<<<<<<< HEAD

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

<<<<<<< HEAD
class CommonMercosulNomenclature(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=5000)
    start_date = models.DateField()
    finish_date = models.DateField()
    act_type = models.CharField(max_length=255)
    act_number = models.CharField(max_length=255)
    act_year = models.IntegerField()

    def __str__(self):
        return self.description

=======
>>>>>>> main
=======

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

>>>>>>> main
