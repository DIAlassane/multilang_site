"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
#toutes les pages du blog
from django.contrib import admin
from django.urls import path
from blog.views import ExtendedFront,switch_to_french, switch_to_english
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('', ExtendedFront, name='ExtendedFront'),
    path('admin/', admin.site.urls),
    path('fr/', switch_to_french, name='switch_to_french'),
    path('en/', switch_to_english, name='switch_to_english'),
)