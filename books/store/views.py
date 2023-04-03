from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from store.models import Book
from store.serializer import BooksSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # permission_classes = [IsAuthenticated]                                          # check  if user logged in
    permission_classes = [IsAuthenticatedOrReadOnly]                                          # check  if user logged in
    filterset_fields = ['price']
    search_fields = ['name', 'author_name']
    ordering_filter = ['price', 'author_name']

    def __str__(self):
        return self.name


# http://127.0.0.1:8000/book/?price=500  # filter = price

# http://127.0.0.1:8000/book/?search=hemingway # search hamingway

# http://127.0.0.1:8000/book/?ordering=price # ordering

def auth(request):
    return render(request, 'OAuth.html')

