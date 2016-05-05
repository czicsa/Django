from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import rentService.templates.template_keys as TemplateKeys
import systemSettingService.data_access.system_setting_keys as SystemSettingKeys
import customerService.data_access.customer_data_access as CustomerDataAccess
import mediaService.data_access.media_data_access as MediaDataAccess
import systemSettingService.data_access.system_setting_data_access as SystemSettingDataAccess
from datetime import datetime, timedelta

def index(request, status):
    template = loader.get_template(TemplateKeys.all_rent)
    all_media = MediaDataAccess.get_all_rented_media()
    medias = []
    if status == "all":
        medias = all_media
    else:
        threshold = int(SystemSettingDataAccess.get_system_setting_by_resource_key(SystemSettingKeys.rent_threshold_days).value)
        for media in all_media:
            if media.rented_date != None and media.rented_date + timedelta(threshold) < datetime.now().date():
                medias.append(media)
    context = {
        'media_list': medias
    }
    return HttpResponse(template.render(context, request))

def make_rent(request):
    return HttpResponseRedirect(reverse('rent:index'))
