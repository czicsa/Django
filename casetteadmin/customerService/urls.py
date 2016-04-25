from django.conf.urls import url

from . import views

app_name = 'customer'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^insertcustomer$', views.insert_customer, name='insertcustomer'),
    url(r'^editcustomer/(?P<customer_id>[0-9]+)/$', views.edit_customer, name='editcustomer'),
    url(r'^updatecustomer/(?P<customer_id>[0-9]+)/$', views.update_customer, name='updatecustomer'),
    url(r'^searchcustomer$', views.search_customer, name='searchcustomer'),
    url(r'^deletecustomer/(?P<customer_id>[0-9]+)/$', views.delete_customer, name='deletecustomer'),
]