# registration/forms.py
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from .models import Entry

class EntryModelForm(ModelForm):
	class Meta:
		model = Entry
		fields = ["email", "first_name", "last_name", "organization", "contact", "notify"]
		labels = {
			"email"			:	_("Email Address"),
			"first_name"	:	_("Given Name"),
			"last_name"		:	_("Last Name"),
			"contact"		:	_("Contact Number"),
			"organization"	:	_("Company/Organization/School"),
			"notify"		:	_("Notify me about upcoming PizzaPy-Cebu Events and Promotions"),
			}
		help_texts = {
			"email"			:	_("<i>Enter a valid email address</i>"),
			"first_name"	:	_("<i>Enter your Given Name</i>"),
			"last_name"		:	_("<i>Enter your Last Name</i>"),
			"contact"		:	_("<i>Enter your Phone or Mobile Number</i>"),
			"organization"	:	_("<i>Enter the Company, Organization, or School you are currently affiliated with</i>"),
			"notify"		:	_("<i>Check to receive notifications of our future events</i>"),
			}