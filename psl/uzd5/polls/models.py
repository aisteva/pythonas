from django.db import models

# Create your models here.


class Vertybe(models.Model):
    vertybe_nr = models.IntegerField()
    pavadinimas = models.CharField(max_length=200)
    vnt = models.CharField(max_length=200)
    kiekis = models.IntegerField()
    suma  = models.DecimalField(max_digits=5, decimal_places=2)
    tikslas = models.CharField(max_length=200, blank =True)


    def __str__(self):
        return self.pavadinimas
    def was_publiched_bigger(self):
        return self.vertybe_nr > 10

class Vieta(models.Model):
    padalinys = models.CharField(max_length=200)
    def __str__(self):
        return self.padalinys


class Narys(models.Model):
    vardas = models.CharField(max_length=200)
    pavarde = models.CharField(max_length=200)
    pareigos = models.CharField(max_length=200)
    def __str__(self):
        return '%s %s' % (self.vardas, self.pavarde)


class Pirkimo_Dokumentas(models.Model):
    pardavejas = models.CharField(max_length=200)
    serija = models.CharField(max_length=200)
    numeris = models.IntegerField()
    pirkimo_data = models.DateTimeField('pirkimo data')
    def __str__(self):
        return self.pardavejas


class Aktas(models.Model):
    pavadinimas = models.CharField(max_length=200, blank=True)
    istaiga = models.CharField(max_length=200)
    data = models.DateTimeField('date published')
    istatymo_nr = models.IntegerField()
    direktorius = models.CharField(max_length=200)
    nariai = models.ManyToManyField(Narys)
    pirkimo_dokumentai = models.ManyToManyField(Pirkimo_Dokumentas)
    vieta = models.ForeignKey(Vieta, on_delete=models.CASCADE)
    vertybe = models.ManyToManyField(Vertybe)    

    def __str__(self):
        return self.pavadinimas
