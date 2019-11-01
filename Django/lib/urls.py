from django.urls import path
from . import views

app_name = 'lib' # 命名空间
urlpatterns = [
  path('', views.home, name="home"),
  path('book/', views.book, name="book"),
  path('addBook/', views.addBook, name='addBook'),
  path('delBook/<int:book_id>', views.deleteBook, name='delBook'),
]