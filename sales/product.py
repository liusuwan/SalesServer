import json
from django.core import serializers
from django.shortcuts import render
from django.shortcuts import HttpResponse

from sales import models


def add(request):
    # product=json.Serializer(request.body)
    print(request.body)
    return render(request, "index.html")


def getproductimage(request):
    sku = request.GET.get("sku", None)
    img = models.ProductImg.objects.get(sku=sku)
    jsondata = json.dumps(img,default=convert_to_builtin_type)
    return HttpResponse(jsondata, content_type="application/json")

def convert_to_builtin_type(obj):
    # 把MyObj对象转换成dict类型的对象
    d = { '__class__':obj.__class__.__name__,
          '__module__':obj.__module__,
        }
    d.update(obj.__dict__)
    return d