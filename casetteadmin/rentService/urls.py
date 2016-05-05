from django.conf.urls import url

from . import views

app_name = 'rent'
urlpatterns = [
    url(r'^(?P<status>[a-z]+)/$', views.index, name='index'),
    url(r'^makerent$', views.make_rent, name='makerent'),
]