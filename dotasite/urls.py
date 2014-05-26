from django.conf.urls import patterns, include, url

from . import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^login/', views.auth_login, name="login"),
    url(r'^logout/', views.auth_logout, name="logout"),
    url(r'^challenge/', views.challenge, name="challenge"),
    url(r'^leaderboard/', include("leaderboard.urls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', views.index, name="index"),
)
