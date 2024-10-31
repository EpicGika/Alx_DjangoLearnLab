from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to display in the list view
    search_fields = ('title', 'author__name')  # Enable search on title and author
    list_filter = ('publication_year',)  # Enable filtering by publication year

admin.site.register(Book, BookAdmin)
