# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models
from django.template.defaultfilters import date


class pocos(models.Model):
    proprietario = models.CharField("proprietario", max_length=254)
    orgao = models.CharField("orgao", max_length=254)
    data_perfuracao = models.DateField("data_perfuracao")
    profundidade = models.FloatField("profundidade")
    q_m3h = models.FloatField("q_m3h")
    equipamento = models.CharField("equipamento", max_length=254)
    geom = models.PointField("geom", srid=4326)

    def __str__(self):
        return self.proprietario

    @property
    def popup_content(self):
        popup = f'<span>Proprietario:{self.proprietario} </span>'
        popup += f'<span>Órgão:{self.orgao} </span>'
        popup += f'<span>Proprietario:{self.profundidade} </span>'
        popup += f'<span>Profundidade (m):{self.q_m3h} </span>'
        popup += f'<span>Equipamento:{self.equipamento} </span>'
        popup += f"<span>Data de Perfuração:{self.data_perfuracao, 'd/m/Y'} </span>"

        return popup