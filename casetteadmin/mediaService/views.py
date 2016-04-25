from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from mediaService.models import Media
from mediaService.data_access import media_data_access as DataAccess
from typeService.data_access import data_access as TypeDataAccess, category_keys as CategoryKeys
import mediaService.templates.template_keys as TemplateKeys

def index(request):
    template = loader.get_template(TemplateKeys.all_media)
    context = {
        'media_list': DataAccess.get_all_media(),
        'media_type_list': TypeDataAccess.get_types_by_category_resource_key(CategoryKeys.media_types_category),
        'media_status_type_list': TypeDataAccess.get_types_by_category_resource_key(CategoryKeys.media_status_types_category),
    }
    return HttpResponse(template.render(context, request))

def insert_media(request):
    media = Media()
    media.media_title = request.POST['media_title']
    media.purchase_date = request.POST['purchase_date']
    media.seq = request.POST['media_seq']
    media.media_type = TypeDataAccess.get_type_by_id(request.POST['media_type'])
    media.status_type = TypeDataAccess.get_type_by_id(request.POST['status_type'])
    DataAccess.insert_media(media)
    return HttpResponseRedirect(reverse('media:index'))

def edit_media(request, media_id):
    template = loader.get_template(TemplateKeys.edit_media)
    context = {
        'media': DataAccess.get_media_by_id(media_id),
        'media_type_list': TypeDataAccess.get_types_by_category_resource_key(CategoryKeys.media_types_category),
        'media_status_type_list': TypeDataAccess.get_types_by_category_resource_key(CategoryKeys.media_status_types_category),
    }
    return HttpResponse(template.render(context, request))

def update_media(request, media_id):
    media = DataAccess.get_media_by_id(media_id)
    media.media_title = request.POST['media_title']
    media.purchase_date = request.POST['purchase_date']
    media.seq = request.POST['media_seq']
    media.media_type = TypeDataAccess.get_type_by_id(request.POST['media_type'])
    media.status_type = TypeDataAccess.get_type_by_id(request.POST['status_type'])
    DataAccess.update_media(media)
    template = loader.get_template(TemplateKeys.all_media)
    return HttpResponseRedirect(reverse('media:index'))


def delete_media(request, media_id):
    media = DataAccess.get_media_by_id(media_id)
    DataAccess.delete_media(media)
    return HttpResponseRedirect(reverse('media:index'))