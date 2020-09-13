from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import municipio_pb

@admin.register(municipio_pb)
class mun_admin(LeafletGeoAdmin):
    list_display = ['nome','cod_ibge_m']
    search_fields = ['nome','cod_ibge_m']
    list_filter = ['cod_ibge_m']

