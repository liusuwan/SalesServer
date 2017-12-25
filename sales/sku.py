from django.core.serializers import json
from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    return render(request, "sales/sku.html")