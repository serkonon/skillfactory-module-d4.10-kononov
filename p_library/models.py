from django.db import models
from django.core.validators import MaxValueValidator


class Author(models.Model):
    full_name = models.TextField(verbose_name="Имя")
    birth_year = models.SmallIntegerField(verbose_name="Год рождения")
    country = models.CharField(max_length=2, verbose_name="Код страны")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField(verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    year_release = models.SmallIntegerField(verbose_name="Год написания")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="book_author")
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name="Цена")
    copy_count = models.PositiveSmallIntegerField(default=1, verbose_name="Кол-во экземпляров")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Publisher(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    books = models.ManyToManyField(Book, through="p_library.Publish")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'

class Publish(models.Model):
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name="publish_publisher")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="publish_book")
    year = models.PositiveSmallIntegerField(validators=[MaxValueValidator(9999)], verbose_name="Год издания")
    copy_count = models.PositiveIntegerField(validators=[MaxValueValidator(999999999)], verbose_name="Тираж")

    def __str__(self):
        return str(self.publisher) + " - " + str(self.book) + " - " + str(self.year)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
