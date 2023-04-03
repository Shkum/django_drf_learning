from unittest import TestCase
from store.serializer import BooksSerializer

from store.models import Book


class BooksSerializerTestCase(TestCase):
    def test_ok(self):
        book1 = Book.objects.create(name='Test book 1', price=500, author_name='Hemingway')
        book2 = Book.objects.create(name='Test book 2', price=200, author_name='TestAuthor4')
        data = BooksSerializer([book1, book2], many=True).data
        expected_data = [
            {
                'id': book1.id,
                'name': 'Test book 1',
                'price': '500.00',
                'author_name': 'Hemingway',

            },
            {
                'id': book2.id,
                'name': 'Test book 2',
                'price': '200.00',
                'author_name': 'TestAuthor4',
            }
        ]
        self.assertEqual(expected_data, data)

