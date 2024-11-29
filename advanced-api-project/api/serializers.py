from rest_framework import serializers
from .models import Author, Book

# Serializer for Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Serialize all fields

    # Custom validation to ensure publication_year is not in the future
    def validate_publication_year(self, value):
        import datetime
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# Serializer for Author model
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serialization of related books

    class Meta:
        model = Author
        fields = ['name', 'books']  # Serialize name and related books



# BookSerializer: Serializes all fields of the Book model and includes custom validation for publication_year.
# AuthorSerializer: Serializes the name of the author and dynamically serializes the related books using a nested BookSerializer.
