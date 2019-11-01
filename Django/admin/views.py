from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse

from django.conf import settings
# from libs.models import Book


def login(request):
  p = request.path
  h = request.get_host()
  m = request.method
  
  return HttpResponse("hello admin </br>" + p + '</br>' +  m)

def img(request):
  image_data = open(settings.BASE_DIR + "/admin/templates/imgs/bak.png", "rb").read()
  return HttpResponse(image_data, content_type="image/png")


def get(request):
  # book_list = Book.objects.order_by('-pub_date')
  # response = JsonResponse(book_list)
  response = JsonResponse({'foo': 'bar'})
  return HttpResponse(response)