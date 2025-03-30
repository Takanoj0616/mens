from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def google_maps(request):
    template = loader.get_template('google_maps.html')
    context = {}
    return HttpResponse(template.render(context, request))