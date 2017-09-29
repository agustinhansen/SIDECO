from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.sideco_home),
    url(r'^user/new/$', views.user_new, name='user_new'),
    url(r'^user/(?P<pk>[0-9]+)/edit/$', views.user_edit, name='user_edit'),
]
