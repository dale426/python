from django.urls import path
from . import views

app_name= 'ad'
urlpatterns = [
  path('', views.login, name='login'),
  path('img', views.img, name='img'),
  path('get', views.get, name='get'),
]