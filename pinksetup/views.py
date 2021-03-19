from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template.response import TemplateResponse


def home(request):
    return TemplateResponse(request, 'index.html')