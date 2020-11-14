# from django.contrib import admin
from django.urls import path
from . import views
from .views import AuthorEdit, AuthorUpdate, AuthorList, author_create_many, books_authors_create_many, FriendEdit, \
    FriendList

app_name = 'p_library'
urlpatterns = [
    path('author/create', AuthorEdit.as_view(), name='author_create'),
    path('authors/<int:pk>/edit', AuthorUpdate.as_view(), name='author_edit'),
    path('author/create_many', author_create_many, name='author_create_many'),
    path('author_book/create_many', books_authors_create_many, name='author_book_create_many'),
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('friend/create', FriendEdit.as_view(), name='friend_create'),
    path('friends/', FriendList.as_view(), name='friend_list'),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),
    path('index/book_borrow/', views.book_borrow),
    path('publishers/', views.publishers),
]