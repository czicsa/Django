from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import loader
import customerService.templates.template_keys as TemplateKeys
from customerService.models import Customer
import customerService.data_access.customer_data_access as DataAccess


def index(request):
    template = loader.get_template(TemplateKeys.all_customer)
    context = {
        'customer_list': DataAccess.get_all_customer(),
    }
    return HttpResponse(template.render(context, request))

def add_customer(request):
    template = loader.get_template(TemplateKeys.add_customer)
    context = {
    }
    return HttpResponse(template.render(context, request))

def insert_customer(request):
    customer = Customer()
    customer.name = request.POST['name']
    customer.customer_identifier = 'sasd'
    customer.phone_number = request.POST['phone']
    customer.personal_identifier = request.POST['pid']
    customer.address = request.POST['address']
    DataAccess.insert_customer(customer)
    return HttpResponseRedirect(reverse('customer:index'))
