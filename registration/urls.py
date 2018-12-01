# registration/urls.py
from django.urls import path
from .views import RegisterPageView, RegisterSuccessPageView
from django.conf import settings

urlpatterns = [
	path("success", RegisterSuccessPageView.as_view(), name='register_success'),
	path('', RegisterPageView.as_view(), name='register'),
]