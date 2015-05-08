"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from polls.views import HelloTemplate
admin.autodiscover()

#urlpatterns = [
 #   url(r'^admin/', include(admin.site.urls)),
#]
urlpatterns =patterns('',
	 url(r'^articles/',include('article.urls')),
     url(r'^admin/',include(admin.site.urls)),
	 url(r'^$' , 'polls.views.home'),
     url(r'^hello/$' , 'polls.views.hello'),
     url(r'^hello_template/$' , 'polls.views.hello_template'),
     url(r'^hello_template_simple/$' , 'polls.views.hello_template_simple'),
     url(r'^hello_class_view/$' , HelloTemplate.as_view()),
     url(r'^accounts/login/$','mysite.views.login'),#django_test module folder in views file looks for method login
     url(r'^accounts/auth/$','mysite.views.auth_view'),
     url(r'^accounts/logout/$','mysite.views.logout'),
     url(r'^accounts/loggedin/$','mysite.views.loggedin'),
     url(r'^accounts/invalid/$','mysite.views.invalid_login'),
     url(r'^accounts/register/$','mysite.views.register_user'),
     url(r'^accounts/register_success/$','mysite.views.register_success'),


 )