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
    naudotojas = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.padalinys


class Narys(models.Model):
    PAREIGOS_CHOICES = (
        ('pirmininkas', 'Komisijos pirmininkas'),
        ('narys', "Narys"),
    )
    vardas = models.CharField(max_length=200)
    pavarde = models.CharField(max_length=200)
    pareigos = models.CharField(max_length=200, choices = PAREIGOS_CHOICES,)
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
    pirmininkas = models.ForeignKey(Narys, on_delete=models.CASCADE, blank=True, null=True)
    nariai = models.ManyToManyField(Narys, related_name = 'Narys',  blank=True)
    pirkimo_dokumentai = models.ManyToManyField(Pirkimo_Dokumentas)
    vieta = models.ForeignKey(Vieta, on_delete=models.CASCADE)
    vertybe = models.ManyToManyField(Vertybe)
    menesis = models.IntegerField(blank = True, null=True)
    metai = models.IntegerField(blank = True, null=True)

    def __str__(self):
        return self.pavadinimas



