from django.http import HttpResponse
from django.shortcuts import render

def index_views(request):
    return HttpResponse("Hello World")