from django.urls import path
from . import views

app_name = "mangalib"

urlpatterns = [
    path("", views.index, name="manga"),
    path("book/<int:id_book>", views.book, name="book"),
    path("author/<int:id_author>", views.author, name="author"),
    path("book/add", views.addBook, name="add-book"),
    path("book/edit/<int:id_book>", views.editBook, name="edit-book"),
    path("author/add", views.addAuthor, name="add-author"),
    path("book/remove/<int:id_book>", views.removeBook, name="remove-book")
]