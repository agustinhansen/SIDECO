from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.sideco_home),
    url(r'^user/new/$', views.user_new, name='user_new'),
]
