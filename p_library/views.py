from django.shortcuts import render
# from django.http import HttpResponse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.forms import formset_factory
from p_library.models import Book, Publisher, Author, Friend
from p_library.forms import AuthorForm, BookForm, FriendForm


def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)


def index(request):
    template = loader.get_template('index.html')
    books_count = Book.objects.all().count()
    books = Book.objects.all().order_by("id")
    friends = Friend.objects.all().order_by("id")
    out_data = {
        "title": "Моя библиотека",
        "books_count": books_count,
        "books": books,
        "friends": friends,
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


def book_borrow(request):
    if request.method == 'POST':
        book_id = request.POST['book_id']
        friend_id = request.POST['friend_id']
        if not book_id or not friend_id:
            return redirect('/index/')
        else:
            book = Book.objects.get(id=book_id)
            friend = None
            if friend_id != "---":
                friend = Friend.objects.get(id=friend_id)
            if not book:
                return redirect('/index/')
            book.friend = friend
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
    out_data = {
        "publishers": publishers,
        "title": "Издатели",
    }
    return HttpResponse(template.render(out_data, request))


class AuthorEdit(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'author_edit.html'

    def get_context_data(self, **kwargs):
        context = super(AuthorEdit, self).get_context_data(**kwargs)
        context['title'] = "Создание данных автора"
        return context


class AuthorList(ListView):
    model = Author
    template_name = 'authors.html'

    def get_context_data(self, **kwargs):
        context = super(AuthorList, self).get_context_data(**kwargs)
        context['title'] = "Авторы"
        return context


class FriendEdit(CreateView):
    model = Friend
    form_class = FriendForm
    success_url = reverse_lazy('p_library:friend_list')
    template_name = 'friend_edit.html'

    def get_context_data(self, **kwargs):
        context = super(FriendEdit, self).get_context_data(**kwargs)
        context['title'] = "Создание данных друга"
        return context


class FriendList(ListView):
    model = Friend
    template_name = 'friends.html'

    def get_context_data(self, **kwargs):
        context = super(FriendList, self).get_context_data(**kwargs)
        context['title'] = "Друзья"
        return context


def author_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=2)  #  Получим класс, который будет создавать формы
    if request.method == 'POST':  #  POST запрос будет содержать в себе заполненные данные формы
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')  #  Здесь мы заполняем формы формсета теми данными, которые пришли в запросе. Обратите внимание на параметр `prefix`. Мы можем иметь на странице не только несколько форм, но и разных формсетов, этот параметр позволяет их отличать в запросе.
        if author_formset.is_valid():  #  Проверяем, валидны ли данные формы
            for author_form in author_formset:
                author_form.save()  #  Сохраним каждую форму в формсете
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))  #  После чего, переадресуем браузер на список всех авторов.
    else:  #  GET запрос, значит в ответ нужно просто "нарисовать" формы
        author_formset = AuthorFormSet(prefix='authors')  #  Инициализируем формсет и ниже передаём его в контекст шаблона
    return render(request, 'manage_authors.html', {'author_formset': author_formset, 'title': 'Создание авторов',})


def books_authors_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=2)
    BookFormSet = formset_factory(BookForm, extra=2)
    if request.method == 'POST':
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')
        book_formset = BookFormSet(request.POST, request.FILES, prefix='books')
        if author_formset.is_valid() and book_formset.is_valid():
            for author_form in author_formset:
                author_form.save()
            for book_form in book_formset:
                book_form.save()
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))
    else:
        author_formset = AuthorFormSet(prefix='authors')
        book_formset = BookFormSet(prefix='books')
    return render(
        request,
        'manage_books_authors.html',
        {
            'author_formset': author_formset,
            'book_formset': book_formset,
            'title': 'Создание авторов и книг',
        }
    )
