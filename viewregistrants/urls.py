# viewregistrants/urls.py
from django.urls import path
from .views import ViewRegistrantListView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
	path('login/', LoginView.as_view(template_name='viewregistrants_login.html'), name='viewregistrants_login'),
	path('logout/', LogoutView.as_view(), name='viewregistrants_logout'),
	path('', ViewRegistrantListView.as_view(), name='viewregistrants_proper'),
]