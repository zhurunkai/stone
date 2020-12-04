from django.urls import path
from . import views

urlpatterns = [
    path('<int:page>', views.list_page, name='list'),
    path('content/<int:post_id>', views.content_page, name='content'),
    path('release/', views.release, name='release'),
    path('search/', views.search, name='search'),
    path('comment/<int:post_id>', views.follow, name='follow')

]
