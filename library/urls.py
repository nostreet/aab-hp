from django.conf.urls import url
from library import views

urlpatterns = [
    url(r'^books/$', views.BookListView.as_view(), name='books'),
]
