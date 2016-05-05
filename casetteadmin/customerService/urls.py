from django.conf.urls import url

from . import views

app_name = 'customer'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^insertcustomer$', views.insert_customer, name='insertcustomer'),
    url(r'^editcustomer/(?P<customer_id>[0-9]+)/$', views.edit_customer, name='editcustomer'),
    url(r'^updatecustomer/(?P<customer_id>[0-9]+)/$', views.update_customer, name='updatecustomer'),
    url(r'^searchcustomer$', views.search_customer, name='searchcustomer'),
    url(r'^deletecustomer/(?P<customer_id>[0-9]+)/$', views.delete_customer, name='deletecustomer'),
    url(r'^customerdatasheet/(?P<customer_id>[0-9]+)/$', views.customer_sheet, name='customerdatasheet'),
    url(r'^rentmedia/(?P<customer_id>[0-9]+)/$', views.rent_media, name='rentmedia'),
    url(r'^unrentmedia/(?P<customer_id>[0-9]+)/(?P<media_id>[0-9]+)/(?P<from_site>[a-z]+)/$', views.unrent_media, name='unrentmedia'),
]