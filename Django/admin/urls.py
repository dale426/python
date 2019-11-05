from django.urls import path
from . import views

app_name= 'ad'
urlpatterns = [
  path('', views.login, name='login'),
  path('img', views.img, name='img'),
  path('get', views.get, name='get'),
  path('getjson', views.getjson, name='getjson'),
  path('getjson2', views.getjson2, name='getjson2'),
  path('getjson3', views.getjson3, name='getjson3'),
  path('http', views.http, name='http'),
]