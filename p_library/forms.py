from django import forms
from django.forms import formset_factory
from .models import Author, Book, Friend


class AuthorForm(forms.ModelForm):
    full_name = forms.CharField(label="ФИО", widget=forms.TextInput)

    class Meta:
        model = Author
        fields = '__all__'


class BookForm(forms.ModelForm):
    title = forms.CharField(label="Название", widget=forms.TextInput)

    class Meta:
        model = Book
        fields = '__all__'


class FriendForm(forms.ModelForm):
    full_name = forms.CharField(label="ФИО", widget=forms.TextInput)

    class Meta:
        model = Friend
        fields = '__all__'


# AuthorFormSet = formset_factory(AuthorForm)
# BookFormSet = formset_factory(BookForm)
