"""
URL configuration for accounting project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
    path('', include('home0.urls')),
    path('customer/', include('customer0.urls')),
    path('chek/', include('chek0.urls')),
    path('factor/', include('factor0.urls')),
]


# python manage.py cleanup_unused_media ? pip install django-unused-media
# find . -name "*.pyc" -delete
# python manage.py flush
# python manage.py migrate factor0 zero
