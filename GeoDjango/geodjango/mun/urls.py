from django.urls import path
from . import views as v

app_name = 'mun'

urlpatterns = [
    path('geojson/', v.munGeoJson.as_view(),name='mun_geojson')
]