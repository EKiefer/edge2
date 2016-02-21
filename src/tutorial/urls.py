# urls.py
from django.conf.urls import url
from .views import TestView

urlpatterns = [
    url(r'^test/', TestView.as_view()),
]



# url(r'^test/$', TemplateView.as_view(template_name=""))