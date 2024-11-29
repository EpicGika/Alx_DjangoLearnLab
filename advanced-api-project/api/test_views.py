from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Book, Author
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test data
        self.author = Author.objects.create(name="John Doe")
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2022,
            author=self.author
        )
        self.client = APIClient()

        # URLs
        self.book_list_url = reverse("book-list")
        self.book_detail_url = reverse("book-detail", args=[self.book.id])

    def test_list_books(self):
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Test Book")

    def test_retrieve_book(self):
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Book")
        self.assertEqual(response.data['publication_year'], 2022)
    
    def test_create_book(self):
        data = {
            "title": "New Book",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post(self.book_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.last().title, "New Book")
    
    def test_update_book(self):
        data = {
            "title": "Updated Book",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.put(self.book_detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")
        self.assertEqual(self.book.publication_year, 2023)

    def test_delete_book(self):
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        response = self.client.get(self.book_list_url, {"publication_year": 2022})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['publication_year'], 2022)

    def test_search_books(self):
        response = self.client.get(self.book_list_url, {"search": "Test"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Test Book")

    def test_ordering_books(self):
        Book.objects.create(title="Another Book", publication_year=2021, author=self.author)
        response = self.client.get(self.book_list_url, {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2021)

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        
        # Option 1: Login using username and password
        self.client.login(username='testuser', password='testpass')
        
        # Option 2: Token-based authentication (if applicable)
        token, created = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        # Set up other test data (e.g., authors and books)
        self.author = Author.objects.create(name="John Doe")
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2022,
            author=self.author
        )    