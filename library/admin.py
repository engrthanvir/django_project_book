from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'publish_date', 'quantity')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('genre', 'publish_date')

admin.site.register(Book, BookAdmin)

