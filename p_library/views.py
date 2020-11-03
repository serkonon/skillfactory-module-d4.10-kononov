# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from p_library.models import Book, Publisher


def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)


def index(request):
    template = loader.get_template('index.html')
    books_count = Book.objects.all().count()
    books = Book.objects.all()
    out_data = {
        "title": "мою библиотеку",
        "books_count": books_count,
        "books": books,
    }
    return HttpResponse(template.render(out_data, request))


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def publishers(request):
    template = loader.get_template('publisher.html')
    publishers = Publisher.objects.all()
    books = Book.objects.all()
    out_data = {
        "publishers": publishers,
        "books": books,
    }
    return HttpResponse(template.render(out_data, request))