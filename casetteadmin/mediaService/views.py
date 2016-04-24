from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from mediaService.models import Media

def index(request):
    template = loader.get_template('./stock.html')
    context = {
        'media_list': Media.objects.all(),
    }
    return HttpResponse(template.render(context, request))