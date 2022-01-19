from django.db import models
from django.db.models.deletion import CASCADE


class ShopCardModel(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование товара')
    description = models.CharField(
        max_length=1000, verbose_name='Описание товара', null=True, blank=True)
    category = models.CharField(
        max_length=100, verbose_name='Категория товара', null=False)
    price = models.PositiveBigIntegerField(
        blank=True, null=True, verbose_name='Цена')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Товар в магазине'
        verbose_name_plural = 'Товар в магазине'


class ShopCardPhotos(models.Model):
    show = models.ForeignKey(
        ShopCardModel, on_delete=models.CASCADE, related_name="shop_images"
    )
    photo = models.ImageField(
        verbose_name='Изображение товара', upload_to='shop-photos')
