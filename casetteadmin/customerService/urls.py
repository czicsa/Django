from django.conf.urls import url

from . import views

app_name = 'customer'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^newcustomer$', views.add_customer, name='newcustomer'),
    url(r'^insertcustomer$', views.insert_customer, name='insertcustomer'),
]