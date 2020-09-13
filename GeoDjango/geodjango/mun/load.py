import os
from django.contrib.gis.utils import LayerMapping
from .models import municipio_pb

# Auto-generated `LayerMapping` dictionary for municipio model
municipio_mapping = {
    'nome': 'nome',
    'cod_ibge_m': 'cod_ibge_m',
    'geom': 'MULTIPOLYGON',
}
shp = os.path.abspath(os.path.join('data','municipios_pb.shp'))

def run_mun (verbose=True):
    lm = LayerMapping(municipio_pb,shp,municipio_mapping)
    lm.save(strict=True,verbose=True)