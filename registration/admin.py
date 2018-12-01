from django.contrib import admin

# Register your models here.
from .models import Entry

class EntryAdmin(admin.ModelAdmin):
	list_display = (
		"email",
		"last_name",
		"first_name",
		"contact",
		"organization",
		"timestamp",
	)

admin.site.register(Entry, EntryAdmin)