from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template.response import TemplateResponse
from pinksetup.models import Pinksetup


def home(request):
    return TemplateResponse(request, 'index.html', {'items': Pinksetup.objects.all()})
