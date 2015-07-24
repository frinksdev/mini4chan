from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add/$', views.add),
    url(r'^post/(?P<pk>[0-9]+)/$', views.view_p),
]
