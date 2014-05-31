from django.conf.urls import patterns, include, url

from . import views

from django.contrib import admin

urlpatterns = patterns(
    url(r'^', views.index, name="index"),
)

