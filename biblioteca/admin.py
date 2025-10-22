from django.contrib import admin
from .models import Author, Book, Review
# Register your models here.

#admin.site.register(Author)
#admin.site.register(Book)
#admin.site.register(Review)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality')
    search_fields = ('name', )
    list_filter = ('nationality', )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author__name',)
    list_filter = ('published_date', 'author',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'rating')
    search_fields = ('book__title', )
    list_filter = ('rating', )