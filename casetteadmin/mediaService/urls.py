from django.conf.urls import url

from . import views

app_name = 'media'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^insertmedia$', views.insert_media, name='insertmedia'),
    url(r'^deletemedia/(?P<media_id>[0-9]+)/$', views.delete_media, name='deletemedia'),
]