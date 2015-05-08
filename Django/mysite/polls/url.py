from django.conf.urls import patterns, include ,url

urlpatterns =patterns('',
	url(r'^all/$','polls.views.polls'),
	url(r'^get/(?P<polls_id>\d+)/$','polls.views.polls'),


)