from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.test, name='other'),
    #url(r'^/$', views.test, name='other'),
    url(r'(?P<id>[0-9]+)/$', views.test, name='question'),
]
