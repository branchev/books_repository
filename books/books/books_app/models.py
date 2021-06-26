from django.db import models


# class Author(models.Model):
#     author = models.CharField(
#         max_length=20,
#     )


class Book(models.Model):
    title = models.CharField(
        max_length=20,
    )
    pages = models.PositiveIntegerField(
        default=0
    )
    description = models.CharField(
        max_length=100,
        default=''
    )
    author = models.CharField(
        max_length=20,
    )
    # author = models.ForeignKey(Author, on_delete=models.CASCADE)

