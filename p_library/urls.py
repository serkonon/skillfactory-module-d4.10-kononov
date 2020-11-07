# from django.contrib import admin
from django.urls import path
from . import views
from .views import AuthorEdit, AuthorList, author_create_many, books_authors_create_many

app_name = 'p_library'
urlpatterns = [
    path('author/create', AuthorEdit.as_view(), name='author_create'),
    path('author/create_many', author_create_many, name='author_create_many'),
    path('author_book/create_many', books_authors_create_many, name='author_book_create_many'),
    path('authors', AuthorList.as_view(), name='author_list'),
    path('index/', views.index),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),
    path('publishers/', views.publishers),
]