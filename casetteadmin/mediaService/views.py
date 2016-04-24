from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from mediaService.models import Media
from mediaService.data_access import media_data_access as DataAccess
import mediaService.templates.template_keys as TemplateKeys

def index(request):
    template = loader.get_template(TemplateKeys.all_media)
    context = {
        'media_list': DataAccess.get_all_media(),
    }
    return HttpResponse(template.render(context, request))

def insert_media(request):
    media = Media()
    media.name = request.POST['media_title']
    DataAccess.insert_media(media)
    return HttpResponseRedirect(reverse('media:index'))


def delete_media(request, media_id):
    media = DataAccess.get_media_by_id(media_id)
    DataAccess.delete_media(media)
    return HttpResponseRedirect(reverse('media:index'))