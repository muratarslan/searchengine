from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import *
import settings

urlpatterns = patterns('',
url(r'^/?$', 'searchengine.views.search'),
)




