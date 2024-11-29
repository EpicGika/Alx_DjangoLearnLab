from django.db import models

# Create your models here.

# Author model representing book authors
class Author(models.Model):
    name = models.CharField(max_length=100)  # Name of the author

    def __str__(self):
        return self.name


# Book model representing books written by authors
class Book(models.Model):
    title = models.CharField(max_length=100)  # Title of the book
    publication_year = models.IntegerField()  # Year the book was published
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')  # One-to-many relationship with Author

    def __str__(self):
        return self.title



# Author model: Represents an author of books. Includes the author's name.
# Book model: Represents a book. Includes the title, publication year, and author (as a ForeignKey relationship).
