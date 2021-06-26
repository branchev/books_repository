"""
The commented code is just for check the program
before the refactoring.
It is clear how the commented code is changed. 
"""


from django.shortcuts import render, redirect

from books.books_app.forms import BookForm
from books.books_app.models import Book


def show_current_page(request, form, template_name):
    if request.method == 'GET':
        context = {
            'form': form,
        }
        return render(request, template_name, context)


def handle_book_from_form(request, form, url_name):
    if form.is_valid():
        form.save()
        return redirect('index')
    return redirect(url_name)


def render_home_page(request):
    books = Book.objects.all()
    return show_current_page(request, books, 'index.html')
    #
    # context = {
    #     'form': books
    # }
    # return render(request, 'index.html', context)


def create_new_book_record(request):
    if request.method == "GET":
        return show_current_page(request, BookForm, 'create.html')
        # context = {
        #     'form': BookForm(),
        # }
        # return render(request, 'create.html', context)
    else:
        form = BookForm(request.POST)
        return handle_book_from_form(request, form, 'create book')
        # if form.is_valid():
        #     form.save()
        #     return redirect('index')
        # return redirect('create book')


def edit_book_record(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        return show_current_page(
            request,
            BookForm(initial=book.__dict__),
            'edit.html'
        )
        # context = {
        #     'form': BookForm(
        #         initial=book.__dict__,
        #     ),
        # }
        # return render(request, 'edit.html', context)
    else:
        form = BookForm(
            request.POST,
            instance=book,
        )
        return handle_book_from_form(request, form, 'edit book')
        # if form.is_valid():
        #     form.save()
        #     return redirect('index')
        # return redirect('edit book')
