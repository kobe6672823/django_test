from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<poll_id>\d+)/$', views.detail, name = 'detail'),
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name = 'results'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name = 'vote'),
    url(r'^test_req/$', views.test_req, name = 'test_req'),
    url(r'^test_json/$', views.test_json, name = 'test_json'),
)
