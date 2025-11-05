from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import AuthorSerializer, BookSerializer, ReviewSerializer
from rest_framework.response import Response
from .models import Author

class AuthorViewSet(viewsets.Viewset):
    def list(self, request):
        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)
