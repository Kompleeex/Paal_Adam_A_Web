from django.db import models

class Kategoria(models.Model):
    kategorianev = models.CharField(verbose_name = "kategorianev", max_length=50)

    def __str__(self):
        return self.kategorianev
    

class Teszt(models.Model):
    kerdes = models.CharField(verbose_name = "kerdes", max_length=50)
    v1 = models.CharField(verbose_name = "valasz1", max_length=50) 
    v2 = models.CharField(verbose_name = "valasz2", max_length=50) 
    v3 = models.CharField(verbose_name = "valasz3", max_length=50) 
    v4 =models.CharField(verbose_name = "valasz4", max_length=50) 
    kategoriaID = models.ForeignKey(Kategoria, verbose_name="kategoria_id_kulsokulcs", on_delete=models.CASCADE)

    def __str__(self):
        return self.kerdes
    
