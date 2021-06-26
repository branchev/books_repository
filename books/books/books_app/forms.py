from django import forms

from books.books_app.models import Book

#
# class AuthorForm(forms.ModelForm):
#     author = forms.CharField(
#         max_length=20,
#     )


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

