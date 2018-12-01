# registration/views.py

from django.shortcuts import render
from .models import Entry
from .forms import EntryModelForm

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

class RegisterPageView(CreateView):
	form_class = EntryModelForm
	model = Entry
	template_name = "register_form.html"

class RegisterSuccessPageView(TemplateView):
	template_name = "register_success.html"
	variable = "variable"