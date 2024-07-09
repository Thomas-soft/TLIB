from django import forms
from .models import Author, Book

class FormAuthor(forms.ModelForm):
    # name = forms.CharField(max_length=32)
    class Meta:
        model = Author
        fields = ["name",]
        labels = {"name": "Name",}

class FormBook(forms.ModelForm):
    # title = forms.CharField(max_length=32)
    # author = forms.ModelChoiceField(queryset=Author.objects.all())
    # quantity = forms.IntegerField()
    class Meta:
        model = Book
        fields = ["title", "author", "quantity"]