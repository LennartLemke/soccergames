from django.db import models

# Create your models here.
class MatchList(models.Model):
    liga = models.CharField(max_length=200)
    spieltag = models.CharField(max_length=200)
    datum = models.DateTimeField('date')
    spielart = models.CharField(max_length=200)
    heimmannschaft = models.CharField(max_length=200)
    auswaertsmannschaft = models.CharField(max_length=200)
    matchlink = models.CharField(max_length=200)