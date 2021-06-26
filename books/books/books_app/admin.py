from django.contrib import admin

from books.books_app.models import Book


#
# admin.site.register(Book)
# admin.site.register(Author)

# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

