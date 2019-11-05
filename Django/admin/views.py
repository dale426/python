import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.shortcuts import render

import json
from django.core import serializers

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse

from django.conf import settings
from lib.models import Book


def login(request):
  p = request.path
  h = request.get_host()
  m = request.method
  
  return HttpResponse("hello admin </br>" + p + '</br>' +  m)

# 返回图片
def img(request):
  image_data = open(settings.BASE_DIR + "/admin/templates/imgs/bak.png", "rb").read()
  return HttpResponse(image_data, content_type="image/png")


def get(request):
  response = JsonResponse({'foo': 'bar'})
  return HttpResponse(response)

# 转json方法一: 
def getjson(request):
  book_list = Book.objects.order_by('-pub_date')
  data = {}
  data['code'] = 200
  data['msg'] = "查询方式 ：json.loads(serializers.serialize('json', book_list))"
  data['data'] = json.loads(serializers.serialize('json', book_list))
  return JsonResponse(data, safe=False)

# 转json方法2
def getjson2(request):
  data = {}
  book_list = Book.objects.all().values()
  data['data'] = list(book_list)
  return JsonResponse(data, safe=False)

# 转json方法3
def getjson3(request):
  data = []
  book_list = Book.objects.all().values()
  for item in book_list:
    data.append(item)
  return JsonResponse(data, safe=False)



import urllib

def http(request):
  res = urllib.request.urlopen('http://www.kuaidi100.com/query?type=yuantong&postid=11111111111', data=None, timeout=10)
  return HttpResponse(res)