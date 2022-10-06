from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    print([(i.id, i.name, i.author, i.pub_date) for i in Book.objects.all()])
    context = {}
    return render(request, template, context)

def books(request):
    template = 'books/books_list2.html'
    context = {'books': Book.objects.all()}
    return render(request, template, context)

def book_view(request, data="2018-09-07"):
    template = 'books/books_list3.html'
    #.filter(order_by='-pub_date')
    books_list = Book.objects.all().filter(pub_date=data)
    books = books_list.all().order_by('-pub_date')

    if prev := Book.objects.filter(pub_date__lt=data).last():
        prev = str(prev.pub_date)
    else:
        prev = ''
    if next := Book.objects.filter(pub_date__gt=data).first():
        next = str(next.pub_date)
    else:
        next = ''
    paginator = Paginator(books, 1)
    page = paginator.get_page(1)
    context = {'page': page,
               'prev_date': prev,
               'next_date': next,
               }
    return render(request, template, context)