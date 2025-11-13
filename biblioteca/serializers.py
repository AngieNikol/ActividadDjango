from rest.framework import serializers
from .models import Author, Book, Review

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'

class BookSerializer(serializers.ModelSerializer):
    recent_reviews=serializers.SerializerMethodField()
    author_name=serializers.ReadOnlyFields(source="author.name")

    class Meta:
        model=Book
        fields='__all__'

    def get_recent_views(self, obj):
        reviews=obj.review_set.order_by('-date')[:5]

class ReviewSerializer(serializers.ModelSerializers):
    class Meta:
        model=Review
        fields='__all__'