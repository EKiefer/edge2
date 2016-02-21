from django.views import generic
from dal import autocomplete

from tutorial.models import Country


class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"
    

# class CountryAutocomplete(autocomplete.Select2QuerySetView):
#     def get_queryset(self):
#         # Don't forget to filter out results depending on the visitor !
#         if not self.request.user.is_authenticated():
#             return Country.objects.none()

#         qs = Country.objects.all()

#         if self.q:
#             qs = qs.filter(name__startswith=self.q)

#         return qs
