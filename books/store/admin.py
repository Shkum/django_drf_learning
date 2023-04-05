from django.contrib import admin

from store.models import Book, UserBookRelation


# admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'author_name']


@admin.register(UserBookRelation)
class UserBookRelationAdmin(admin.ModelAdmin):
    pass