from rest_framework import serializers
from .models import Book, Borrower


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'is_borrowed']


class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = ['name', 'user', 'book']
