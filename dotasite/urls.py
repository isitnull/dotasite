from django.conf.urls import patterns, include, url

from . import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dotasite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/', views.login, name="login"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', views.index, name="index"),
)
