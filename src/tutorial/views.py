from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic import View
from dal import autocomplete

from .models import Country
from .forms import PersonForm

class CountryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated():
        #     return Country.objects.none()

        qs = Country.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

class TestView(View):
	template_name = "tutorial/tutorial.html"
	form_class = PersonForm

	def get(self, request):
		form = self.form_class()

		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
		
		return render(request, self.template_name, {'form': form})