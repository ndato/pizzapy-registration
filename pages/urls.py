# pages/urls.py
from django.urls import path
from .views import HomePageView
from django.conf import settings

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
]