"""
URL configuration for StarLabs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from apps.views import homepage_view, base_view, urmat_view, sierra_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_view, name='homepage'),
    path('base/', base_view, name='base'),
    path('urmat/', urmat_view, name='urmat'),
    path('sierra/', sierra_view, name='sierra'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)