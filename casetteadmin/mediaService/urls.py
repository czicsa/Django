from django.conf.urls import url

from . import views

app_name = 'media'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^insertmedia$', views.insert_media, name='insertmedia'),
    url(r'^editmedia/(?P<media_id>[0-9]+)/$', views.edit_media, name='editmedia'),
    url(r'^updatemedia/(?P<media_id>[0-9]+)/$', views.update_media, name='updatemedia'),
    url(r'^deletemedia/(?P<media_id>[0-9]+)/$', views.delete_media, name='deletemedia'),
    url(r'^mediadatasheet/(?P<media_id>[0-9]+)/$', views.media_sheet, name='mediadatasheet'),
]