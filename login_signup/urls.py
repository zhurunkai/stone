from django.urls import path
from . import views

urlpatterns = [
    path('send_code/', views.send_code),
    path('login/', views.login, name="login"),
    path('register_page/', views.register_page, name='register_page'),
    path('register/', views.register, name="register"),
    path('login_page/', views.login_page, name="login_page")
]
