from django.conf.urls import url,include
from django.contrib import admin
from . import views
from niji import urls as niji_urls
from django.views.generic import TemplateView

urlpatterns = [
    url(r"^$", views.emailView, name="home"),

    url(r"forum/", include(niji_urls, namespace="niji")),

    url(r"^thanks/$", TemplateView.as_view(template_name="thanks.html"),
        name="thanks"),
    url(r"^welcome/$", views.MainPage.as_view(), name="main"),

    url(r"^members/$", views.member_area, name="members"),

    url(r"^hiveware/$", views.HivewarePage.as_view(), name="hiveware"),
    url(r"^suppliers/$", views.SuppliersPage.as_view(), name="suppliers"),
    url(r"^howto/$", views.HowtoPage.as_view(), name="howto"),

    url(r"^admin/", admin.site.urls),

    url(r"^accounts/", include("accounts.urls", namespace="accounts")),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^library/', include('library.urls', namespace='library')),
    url(r'^conference/', include('beeexpo.urls', namespace='beeexpo')),

    # url(r"^committee/$", views.contact_area, name="contact"),

]
