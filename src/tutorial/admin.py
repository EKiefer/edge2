from django.contrib import admin
from .models import Country, Person
from .forms import PersonForm

admin.site.register(Country)

class PersonAdmin(admin.ModelAdmin):
	form = PersonForm
admin.site.register(Person, PersonAdmin)
# Register your models here.
