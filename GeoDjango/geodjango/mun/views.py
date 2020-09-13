from django.shortcuts import render

from djgeojson.views import GeoJSONLayerView
from .models import municipio_pb

class munGeoJson(GeoJSONLayerView):
    model = municipio_pb
    properties = ('popup_content',)
