from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import pocos

@admin.register(pocos)
class pocos_admin(LeafletGeoAdmin):
    list_display = ['proprietario', 'orgao', 'profundidade', 'q_m3h', 'equipamento']
    search_fields = ['proprietario', 'orgao']
    list_filter = ['equipamento']