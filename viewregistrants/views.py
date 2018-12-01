from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from registration.models import Entry

class ViewRegistrantListView(ListView):
	model = Entry
	template_name = "viewregistrants_list.html"
	ordering = "timestamp"
	context_object_name = "Entry"
	#paginate_by = 100