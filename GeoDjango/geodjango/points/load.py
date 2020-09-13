import os
from django.contrib.gis.utils import LayerMapping
from .models import pocos

# Auto-generated `LayerMapping` dictionary for pocos model
pocos_mapping = {
    'proprietario': 'proprietar',
    'orgao': 'orgao',
    'data_perfuracao': 'data_perfu',
    'profundidade': 'profundida',
    'q_m3h': 'q_m3h',
    'equipamento': 'equipament',
    'geom': 'POINT',
}

shp = 'C:/Users/leona/PycharmProjects/GeoDjango/data/pocos.shp'

def run_pocos (verbose=True):
    lm = LayerMapping(pocos,shp,pocos_mapping)
    lm.save(strict=True,verbose=True)