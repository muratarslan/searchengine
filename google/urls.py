from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import *

urlpatterns = patterns('',
(r'^/?$', 'searchengine.views.search'),
)
