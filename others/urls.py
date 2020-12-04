from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name="about"),
    path('complain/', views.write_advice, name='complain'),
    path('media/', views.media, name='media'),
    path('newmain/', views.newmain, name='newmain'),
    path('user/', views.user1, name='user1'),
    path('user2/', views.user2, name='user2'),
    path('stone/', views.stone, name='shimo'),
    path('main_part/', views.main_part, name='main_part')
]
