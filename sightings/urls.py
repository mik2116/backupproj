
from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from . import views


urlpatterns = [
        path('map/',views.showmap, name = 'showmap'),
        path('sightings/add', views.add, name='add'),
        path('sightings/stats', views.stats, name='stats'),
        path('sightings/sightings', views.sightings, name='sightings'),
        path('sightings/<unique_squirrel_id>', views.update, name='update'),
    ]


