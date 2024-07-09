from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Author, Book
from .forms import FormAuthor, FormBook

# Create your views here.
def index(request):
    context = {
        "books": Book.objects.all(),
    }
    return (render(request, "mangalib/index.html", context))

def book(request, id_book):
    context = {
        "book": get_object_or_404(Book, pk=id_book),
    }
    return (render(request, "mangalib/book.html", context))

def author(request, id_author):
    context = {
        "author": get_object_or_404(Author, pk=id_author),
    }
    return (render(request, "mangalib/author.html", context))

def editBook(request, id_book):
    book = Book.objects.get(pk=id_book)
    if (request.method == "POST"):
        form = FormBook(request.POST, instance = book)
        if (form.is_valid()):
            form.save()
            return (redirect("mangalib:manga"))
    else:
        form = FormBook(instance=book)
    context = {
        "form": form
    }
    return (render(request, "mangalib/addBook.html", context))

def addAuthor(request):
    if (request.method == "POST"):
        form = FormAuthor(request.POST)
        if (form.is_valid()):
            form.save()
            return (redirect("mangalib:manga"))
    else:
        form = FormAuthor()
    context = {
        "form": form,
    }
    return (render(request, "mangalib/addAuthor.html", context))

def addBook(request):
    if (request.method == "POST"):
        form = FormBook(request.POST)
        if (form.is_valid()):
            form.save()
            return (redirect("mangalib:manga"))
    else:
        form = FormBook()
    context = {
        "form": form,
    }
    return (render(request, "mangalib/addBook.html", context))

def removeBook(request, id_book):
    book = Book.objects.get(pk=id_book)
    book.delete()
    return (redirect("mangalib:manga"))