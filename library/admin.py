from django.contrib import admin
from .models import Book, Review, BookHistory

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(BookHistory)
