from django.db import models

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

