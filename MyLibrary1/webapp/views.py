from rest_framework import viewsets, request, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer, BorrowerSerializer
from .models import Book, Borrower


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BorrowerViewSet(viewsets.ModelViewSet):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer


@api_view(['GET'])
def available_book_list(request):
    if request.method == 'GET':
        book = Book.objects.filter(is_borrowed=False)
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def borrow_book(request):
    if request.method == 'GET':
        count = Book.objects.all().count()
        count -= 1
        return Response(count)


@api_view(['POST'])
def return_book(request):
    if request.method == 'POST':
        count = Book.objects.all().count()
        count += 1
        return Response(count)
