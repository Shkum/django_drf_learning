from unittest import TestCase

from django.contrib.auth.models import User
from django.db.models import Count, Case, When, Avg

from store.serializer import BooksSerializer

from store.models import Book, UserBookRelation


class BooksSerializerTestCase(TestCase):
    def test_ok(self):
        user_0 = User.objects.create(username='user_0')
        user_2 = User.objects.create(username='user_2')
        user_3 = User.objects.create(username='user_3')
        book1 = Book.objects.create(name='Test book 1', price=500, author_name='Hemingway')
        book2 = Book.objects.create(name='Test book 2', price=200, author_name='TestAuthor4')

        UserBookRelation.objects.create(user=user_0, book=book1, like=True, rate=5)
        UserBookRelation.objects.create(user=user_2, book=book1, like=True, rate=5)
        UserBookRelation.objects.create(user=user_3, book=book1, like=True, rate=4)

        UserBookRelation.objects.create(user=user_0, book=book2, like=True, rate=3)
        UserBookRelation.objects.create(user=user_2, book=book2, like=True, rate=4)
        UserBookRelation.objects.create(user=user_3, book=book2, like=False)

        books = Book.objects.all().annotate(
            annotated_likes=Count(Case(When(userbookrelation__like=True, then=1))),
            rating=Avg('userbookrelation__rate')
        ).order_by('id')

        # data = BooksSerializer([book1, book2], many=True).data
        data = BooksSerializer(books, many=True).data
        expected_data = [
            {
                'id': book1.id,
                'name': 'Test book 1',
                'price': '500.00',
                'author_name': 'Hemingway',
                'annotated_likes': 3,
                'rating': '4.67',
            },
            {
                'id': book2.id,
                'name': 'Test book 2',
                'price': '200.00',
                'author_name': 'TestAuthor4',
                'annotated_likes': 2,
                'rating': '3.50',
            }
        ]
        self.assertEqual(expected_data, data)
