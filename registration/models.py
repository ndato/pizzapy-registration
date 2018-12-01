#registration/models.py

from django.db import models
from django.urls import reverse

# Create your models here.
class Entry(models.Model):
	email = models.EmailField(max_length = 254, primary_key = True, unique = True, blank = False,
			error_messages={'required': 'Please provide your email address',
							'unique': 'An entry with this email already exists'}
	)
	first_name = models.CharField(max_length = 1024, blank = False, unique = False)
	last_name = models.CharField(max_length = 1024, blank = False, unique = False)
	contact = models.CharField(max_length = 64, blank = False, unique = True,
			error_messages={'required': 'Please provide your contact number',
							'unique': 'An entry with this contact number already exists'}
	)
	organization = models.CharField(max_length = 1024, blank = True)
	notify = models.BooleanField(default = True)
	timestamp = models.DateTimeField(auto_now_add = True, verbose_name="Registered on")
		
	def __str__(self):
		return (f"{self.last_name}, {self.first_name} - {self.timestamp}")
		
	def get_absolute_url(self):
		return reverse('register_success')
		
	class Meta:
		get_latest_by = "timestamp"