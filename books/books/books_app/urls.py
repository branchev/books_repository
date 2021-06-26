from django.urls import path

from books.books_app.views import render_home_page, create_new_book_record, edit_book_record

urlpatterns = [
    path('', render_home_page, name='index'),
    path('create/', create_new_book_record, name='create book'),
    path('edit/<int:pk>', edit_book_record, name='edit book'),
]
