from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=32, unique=True)
    def __str__(self):
        return (self.name)
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

class Book(models.Model):
    title = models.CharField(max_length=32)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    releaseDate = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return (self.title)
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"