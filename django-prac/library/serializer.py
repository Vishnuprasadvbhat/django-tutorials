from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = '__all__'

  def validate_isbn(self, value):
      """Custom validation to ensure the ISBN is 13 characters."""
      if len(value) != 13:
          raise serializers.ValidationError("ISBN must be exactly 13 characters.")
      return value