from django.shortcuts import render
from rest_framework import generics
from .serializer import BookSerializer
from .models import Book


# Create your views here.
def home(request):
  return render(request, 'contents/index.html')



class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
   queryset = Book.objects.all()
   serializer_class = BookSerializer
