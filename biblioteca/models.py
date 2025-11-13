from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)

    def clean(self):
        if not self.name:
            raise ValidationError('El nombre del autor no puede estar vacío.')
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    abstract = models.TextField()

    def clean(self):
        if len(self.abstract)< 30:
            raise ValidationError('El resumen debe tener al menos 30 caracteres.')

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    rating = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )

    #def clean(self):
        #if not (1 <= self.rating <= 5):
            #raise ValidationError('La calificación debe estar entre 1 y 5.')*/

    def __str__(self):
        return f"{self.book.title} - {self.rating}/5"
