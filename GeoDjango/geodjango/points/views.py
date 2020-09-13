from django.shortcuts import render
from djgeojson.views import GeoJSONLayerView
from .models import pocos

class pocosGeoJson(GeoJSONLayerView):
    model = pocos
    properties = ('popup_content',)