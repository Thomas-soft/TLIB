from django.contrib import admin
from .models import Author, Book

# Register your models here.
@admin.register(Author)
class   AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    pass

@admin.register(Book)
class   BookAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author", "quantity"]