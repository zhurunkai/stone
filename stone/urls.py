"""stone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login_signup/', include(('login_signup.urls', 'login_signup'), namespace='login_signup')),
    path('', include(('home.urls', 'home'), namespace='home')),
    path('others/', include(('others.urls', 'others'), namespace='others')),
    path('posts/', include(('posts.urls', 'posts'), namespace='posts')),
    path('manage/', include(('backmanage.urls', 'backmanage'), namespace='backmanage')),
    path('mystone/', include(('mystone.urls', 'mystone'), namespace='mystone')),
    path('fullview/', include(('fullview.urls', 'fullview'), namespace='fullview'))
]
