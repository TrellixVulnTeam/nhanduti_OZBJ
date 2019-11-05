"""nhanduti URL Configuration

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

from apps.core import views as core_views
from apps import organic_fair, organic_farmer, organic_map, accounts


urlpatterns = [
    path('', core_views.IndexView.as_view(template_name='index.html'), name='index'),
    # path('', include('core.urls'), name='index'),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('produtores-organicos/', include('apps.organic_farmer.urls', namespace='organic_farmer')),
    path('feiras-organicas/', include('apps.organic_fair.urls', namespace='organic_fair')),
    path('mapa/', include('apps.organic_map.urls', namespace='organic_map')),
    path('conta/', include('apps.accounts.urls', namespace='accounts')),
    # path('admin/', admin.site.urls),
]
