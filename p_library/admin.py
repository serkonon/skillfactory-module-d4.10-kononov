from django.contrib import admin
from p_library.models import Book, Author, Publisher


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ('author_id',)
    list_display = ('title', 'author')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ('country', 'full_name')


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass
