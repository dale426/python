from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book
from django.urls import reverse
from django.http import JsonResponse

# Create your views here.


def home(request):
    return HttpResponse("this is a lib application")


def book(request):
    book_list = Book.objects.order_by('-pub_date')
    context = {'book_list': book_list}
    return render(request, 'app/detail.html', context)


def addBook(request):
    if request.method == 'POST':
        temp_name = request.POST['name']
        temp_author = request.POST['author']
        temp_pub_house = request.POST['pub_house']

        from django.utils import timezone

        temp_book = Book(name=temp_name, author=temp_author,
                         pub_house=temp_pub_house, pub_date=timezone.now())
        temp_book.save()

        # 重定向
        return HttpResponseRedirect(reverse('lib:book'))


def deleteBook(request, book_id):
    bookID = book_id
    Book.objects.filter(id = bookID).delete()
    return HttpResponseRedirect(reverse('lib:book'))


def updateBook(request, book_id):
    bookID= book_id
    Book.objects.filter(id=bookID).update(name="123")
