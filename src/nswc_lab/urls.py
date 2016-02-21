from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

import profiles.urls
import accounts.urls
import tutorial.urls
from . import views
from tutorial.views import CountryAutocomplete

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^country-autocomplete/$', CountryAutocomplete.as_view(), name='country-autocomplete'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^tutorial/', include(tutorial.urls, namespace='tutorial')),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
