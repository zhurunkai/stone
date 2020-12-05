from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexmystone, name="indexmystone"),
    path('new/', views.newindex, name='newindex'),
    path('savegame/', views.savegame, name='savegame'),
    path('savedata/', views.savedata, name='savedata')
]
