from django.urls import path
from . import views as v

app_name = 'points'

urlpatterns = [
    path('geojson/', v.pocosGeoJson.as_view(),name='poco_geojson')
]