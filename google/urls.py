from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import *

urlpatterns = patterns('',
(r'^/?$', 'google.searchengine.views.search'),
)
