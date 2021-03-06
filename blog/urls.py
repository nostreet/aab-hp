from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^news/$', views.PostListView.as_view(), name='news'),
    url(r'^news/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='news_detail'),

]
