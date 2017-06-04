from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, health
from servis.views import getNalog, servisLogin, servisLogout, servis, getNalogList
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^health/$', health),
    url(r'^servis/get_nalog/$', getNalog),
    url(r'^servis/login/$', auth_views.login),
    url(r'^servis/$', servis),
    url(r'^servis/logout$', servisLogout),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^getNalogList/', getNalogList),
    
]
