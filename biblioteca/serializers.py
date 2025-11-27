from rest_framework import serializers
from .models import Author, Book, Review

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'

class BookSerializer(serializers.ModelSerializer):
    recent_reviews=serializers.SerializerMethodField()
    author_name=serializers.ReadOnlyField(source="author.name")

    class Meta:
        model=Book
        fields='__all__'

    def get_recent_reviews(self, obj):
        reviews=obj.reviews.order_by('-date')[:5]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'