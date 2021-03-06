from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="beeexpo/index.html"),
        name="home"),
    url(r"^c/speakers/$", TemplateView.as_view(template_name="beeexpo/speakers.html"),
        name="speakers"),
    url(r"^c/schedule/$", TemplateView.as_view(template_name="beeexpo/schedule.html"),
        name="schedule"),
    url(r'^c/contact/$', views.emailView, name='contact'),
    url(r'^c/tickets/$', views.showSignUpform, name='tickets'),
]
