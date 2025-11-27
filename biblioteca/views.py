from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import AuthorSerializer, BookSerializer, ReviewSerializer
from rest_framework.response import Response
from .models import Author , Book, Review
from rest_framework.decorators import action
from django.db.models import Avg

class AuthorViewSet(viewsets.ModelViewSet):
        queryset = Author.objects.all()
        serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #filter_backends = ['author']
    filterset_fields = ['author', 'published_date']
    ordering_fields = ['published_date', 'title']

    def get_queryset(self):
        queryset = Book.objects.all()
        author_id = self.request.query_params.get('author')
        year = self.request.query_params.get('year')
        if author_id:
            queryset = queryset.filter(author_id=author_id)
        if year:
            queryset = queryset.filter(published_date__year=year)
        return queryset


    @action(detail=True, methods=['get'])
    def average_rating(self, request, pk=None):
        book = self.get_object()
        avg_rating = book.reviews.aggregate(average=Avg('rating'))['average']
        return Response({'book': book.title, 'average_rating': avg_rating})

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
