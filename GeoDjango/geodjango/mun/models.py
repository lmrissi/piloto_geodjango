# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class municipio_pb(models.Model):
    nome = models.CharField('nome',max_length=40)
    cod_ibge_m = models.CharField('código IBGE',max_length=20)
    geom = models.MultiPolygonField('geom',srid=4326)

    def __str__(self):
        return self.nome

    @property
    def popup_content(self):
        popup = f'<span>Nome:{self.nome} </span>'
        popup += f'<span>Cod_IBGE:{self.cod_ibge_m} </span>'

        return popup