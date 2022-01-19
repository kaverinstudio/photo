from django.test import TestCase
from .models import Photo, MainCardModel
from user.models import UserModel
from django.contrib.auth import get_user_model

User = get_user_model()


class CreateOrderTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        UserModel.objects.create_user(
            'bob', 'bob@test.com', 'fhg23mdhd44')
        Photo.objects.create(
            format='10x15',
            file='/order/username/photo.jpg',
            user=User.objects.get(id=1),
            count='1',
            papier='Глянцевая',
        )

    def test_photo_format(self):
        format = Photo.objects.get(id=1)
        field_label = format._meta.get_field('format').verbose_name
        self.assertEquals(field_label, 'format')

    def test_photo_papier(self):
        papier = Photo.objects.get(id=1)
        field_label = papier._meta.get_field('papier').verbose_name
        self.assertEqual(field_label, 'papier')

    def test_photo_papier_length(self):
        papier = Photo.objects.get(id=1)
        max_length = papier._meta.get_field('papier').max_length
        self.assertEqual(max_length, 20)

    def test_photo_count(self):
        count = Photo.objects.get(id=1)
        field_label = count._meta.get_field('count').default
        self.assertAlmostEquals(field_label, '1')

    def test_photo_user_blank(self):
        user = Photo.objects.get(id=1)
        field_label = user._meta.get_field('user').blank
        self.assertEqual(field_label, True)


class MainCardModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        MainCardModel.objects.create(
            image='photo.jpg',
            description='new_photo',
        )

    def test_main_card_field(self):
        image = MainCardModel.objects.get(id=1)
        field_label = image._meta.get_field('image').upload_to
        self.assertEqual(field_label, 'site-images')

    def test_main_card_field_desc(self):
        description = MainCardModel.objects.get(id=1)
        field_label = description._meta.get_field('description').max_length
        self.assertEqual(field_label, 150)
