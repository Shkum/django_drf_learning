from django.contrib import admin

from store.models import Book


# admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'price', 'author_name']

