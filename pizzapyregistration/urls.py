"""pythonchallenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

admin.site.site_header = "PizzaPy-Cebu Administration Site"
admin.site.site_title = "PizzaPy-Cebu Administration Site"

urlpatterns = [
    path('walangpapasokditotanginakayonglahat/', include('viewregistrants.urls')),
    path('walangpapasokditotanginakayonglahat/admin/', admin.site.urls),
	path('register/', include('registration.urls')),
	path('', include('pages.urls')),
]
