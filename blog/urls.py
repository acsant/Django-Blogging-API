from django.confs.urls import patterns, url
from blog import views
urlpatterns = patterns('',
    url(r'^$', views.BlogViewSet, name='blog_entry')
    url(r'^(?P<data_id>\d+)/$', views.BlogViewSet, name='blog_detail')
)
