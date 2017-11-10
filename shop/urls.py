from django.conf.urls import url
from django.contrib import admin
from shop import views
urlpatterns = [
    url(r'^$', views.index),

    url(r'^(?P<id>[0-9]+)/$', views.shop),

]
