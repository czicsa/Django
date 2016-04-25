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

def insert_customer(request):
    customer = Customer()
    customer.name = request.POST['name']
    customer.phone_number = request.POST['phone']
    customer.personal_identifier = request.POST['pid']
    customer.address = request.POST['address']
    DataAccess.insert_customer(customer)
    return HttpResponseRedirect(reverse('customer:index'))

def edit_customer(request, customer_id):
    template = loader.get_template(TemplateKeys.edit_customer)
    context = {
        'customer': DataAccess.get_customer_by_id(customer_id),
    }
    return HttpResponse(template.render(context, request))

def update_customer(request, customer_id):
    customer = DataAccess.get_customer_by_id(customer_id)
    customer.name = request.POST['name']
    customer.phone_number = request.POST['phone']
    customer.personal_identifier = request.POST['pid']
    customer.address = request.POST['address']
    DataAccess.update_customer(customer)
    return HttpResponseRedirect(reverse('customer:index'))

def search_customer(request):
    name = request.POST['name']
    customer_identifier = request.POST['customer_identifier']
    personal_identifier = request.POST['pid']
    result = DataAccess.get_customer_by_name_and_customer_identifier_and_personal_identifier(name,customer_identifier, personal_identifier)

    template = loader.get_template(TemplateKeys.all_customer)
    context = {
        'customer_list': result,
    }
    return HttpResponse(template.render(context, request))

def delete_customer(request, customer_id):
    customer = DataAccess.get_customer_by_id(customer_id)
    DataAccess.delete_customer(customer)
    return HttpResponseRedirect(reverse('customer:index'))
