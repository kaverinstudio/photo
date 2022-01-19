from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import UserModel

User = get_user_model()


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        UserModel.objects.create_user(
            'bob', 'bob@test.com', 'fhg23mdhd44')

    def test_create(self):
        UserModel.objects.create(
            username='Bob',
            email='bob@test.com',
            password='yr56due834S',
        )

    def test_user_name(self):
        name = User.objects.get(id=1)
        label_field = name._meta.get_field('username').max_length
        self.assertEqual(label_field, 150)

    def test_user_name_unique(self):
        password = User.objects.get(id=1)
        label_field = password._meta.get_field('username').unique
        self.assertEqual(label_field, True)
