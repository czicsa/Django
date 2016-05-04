from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import rentService.templates.template_keys as TemplateKeys
import customerService.data_access.customer_data_access as CustomerDataAccess
import mediaService.data_access.media_data_access as MediaDataAccess

def index(request):
    template = loader.get_template(TemplateKeys.all_rent)
    context = {
        'media_list': MediaDataAccess.get_all_rented_media(),
        'customer_list': CustomerDataAccess.get_all_customer(),
    }
    return HttpResponse(template.render(context, request))

def make_rent(request):
    return HttpResponseRedirect(reverse('rent:index'))
