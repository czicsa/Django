from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import loader
import customerService.templates.template_keys as TemplateKeys
import mediaService.templates.template_keys as MediaTemplateKeys
import typeService.data_access.type_keys as TypeKeys
from customerService.models import Customer
import customerService.data_access.customer_data_access as DataAccess
import mediaService.data_access.media_data_access as MediaDataAccess
import typeService.data_access.data_access as TypeDataAccess
from datetime import datetime


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

def customer_sheet(request, customer_id):
    customer = DataAccess.get_customer_by_id(customer_id)
    template = loader.get_template(TemplateKeys.customer_data_sheet)
    context = {
        'customer': customer,
        'rentable_media': MediaDataAccess.get_all_media().filter(status_type_id = TypeDataAccess.get_type_by_resource_key(TypeKeys.rentable))
    }
    return HttpResponse(template.render(context, request))

def rent_media(request, customer_id):
    media_id = request.POST['media']
    customer = DataAccess.get_customer_by_id(customer_id)
    media = MediaDataAccess.get_media_by_id(media_id)
    media.status_type = TypeDataAccess.get_type_by_resource_key(TypeKeys.rented)
    media.rented_date = datetime.now()
    MediaDataAccess.update_media(media)
    customer.medias.add(media)
    template = loader.get_template(TemplateKeys.customer_data_sheet)
    return HttpResponseRedirect(reverse('customer:customerdatasheet', kwargs={'customer_id':customer_id}))

def unrent_media(request, customer_id, media_id, from_site):
    customer = DataAccess.get_customer_by_id(customer_id)
    media = customer.medias.get(id=media_id)
    media.status_type = TypeDataAccess.get_type_by_resource_key(TypeKeys.rentable)
    media.rented_date = None
    MediaDataAccess.update_media(media)
    customer.medias.remove(media)
    if from_site == "media":
        template = loader.get_template(MediaTemplateKeys.all_media)
        return HttpResponseRedirect(reverse('media:index'))
    else:
        template = loader.get_template(TemplateKeys.customer_data_sheet)
        return HttpResponseRedirect(reverse('customer:customerdatasheet', kwargs={'customer_id':customer_id}))

