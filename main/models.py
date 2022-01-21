import json
from django.db import models
from django.db.models.deletion import CASCADE


class MainCardModel(models.Model):
    image = models.ImageField(upload_to='site-images',
                              verbose_name='Изображение')
    description = models.TextField(max_length=150, verbose_name='Описание')
    post_link = models.URLField(max_length=200)

    def __str__(self):
        return f'{self.description}'

    class Meta:
        verbose_name = 'Карточка на главной странице'
        verbose_name_plural = 'Карточки на главной странице'


def user_directory_path(instance, filename):
    if instance.user:
        return 'orders/%s_%s/%s' % (instance.user.username, instance.user.email, filename)
    return 'orders/%s/%s' % (instance.session_key, filename)


class Services(models.Model):
    name = models.CharField(max_length=50, blank=True, unique=True,
                            null=True, verbose_name='Услуга')
    cost = models.PositiveBigIntegerField(
        blank=True, null=True, verbose_name='Цена')

    def __str__(self) -> str:
        return f'{self.name}'

    @classmethod
    def to_json(cls):
        services = {s.name: s.cost for s in cls.objects.all()}
        return json.dumps(services)

    class Meta:
        verbose_name = 'Услуга и цена'
        verbose_name_plural = 'Услуги и цены'


class Photo(models.Model):
    FORMATS = [
        ('10x15', '10x15'),
        ('15x21', '15x21'),
        ('20x30', '20x30'),
    ]

    PAPIER = [
        ('Глянцевая', 'Глянцевая'),
        ('Матовая', 'Матовая'),
    ]

    format = models.CharField(
        choices=FORMATS, max_length=100, default='10x15', blank=True)
    file = models.ImageField(upload_to=user_directory_path)
    session_key = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(
        'user.UserModel', on_delete=models.SET_NULL, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    count = models.PositiveBigIntegerField(blank=True, null=True, default='1')
    papier = models.CharField(
        choices=PAPIER, max_length=20, default='Глянцевая', blank=True)

    @classmethod
    def get_user_photos(cls, request):
        if request.user.is_anonymous:
            return cls.objects.filter(session_key=request.session.session_key)

        return (
            cls.objects
            .filter(
                models.Q(user=request.user)
                | models.Q(session_key=request.session.session_key)
            )
        )

    class Meta:
        verbose_name = 'Фотографии заказа'
        verbose_name_plural = 'Фотографии заказов'


class Orders(models.Model):
    user = models.ForeignKey(
        to='user.UserModel', on_delete=models.CASCADE, blank=True, null=True)
    order_session_key = models.CharField(max_length=100, blank=True, null=True)
    order_count = models.PositiveBigIntegerField(blank=True, null=True)
    order_format = models.CharField(max_length=10, null=True, blank=True)
    order_papier = models.CharField(max_length=20, blank=True, null=True)

    @classmethod
    def get_order_photos(cls, request):
        if request.user.is_anonymous:
            return cls.objects.filter(order_session_key=request.session.session_key)

        return (
            cls.objects
            .filter(
                models.Q(user=request.user)
                | models.Q(order_session_key=request.session.session_key)
            )
        )

    class Meta:
        verbose_name = 'Временный заказ'
        verbose_name_plural = 'Временные заказы'


class ConfirmOrder(models.Model):

    # image = models.ImageField()
    user = models.ForeignKey(
        to='user.UserModel', on_delete=CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, null=True,
                            blank=True, verbose_name='Имя заказчика')
    phone = models.CharField(null=True, blank=True,
                             max_length=20, verbose_name='Телефон заказчика')
    delivery = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='Способ доставки')
    address = models.CharField(
        max_length=200, blank=True, null=True, verbose_name='Адрес доставки')
    comment = models.CharField(
        max_length=500, blank=True, null=True, verbose_name='Комментарии к заказу')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время заказа')
    link = models.FilePathField(blank=True, null=True, allow_folders=True, verbose_name='Папка с заказом')
    session_key = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = 'Сформированный заказ'
        verbose_name_plural = 'Сформированные заказы'


class Portfolio(models.Model):
    photo_title = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Категория фото')

    def __str__(self):
        return f'{self.photo_title}'

    class Meta:
        verbose_name = 'Фотография в портфолио'
        verbose_name_plural = 'Фотографии в портфолио'


class PortfolioPhoto(models.Model):
    showphoto = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name="images")
    photo = models.ImageField(upload_to='portfolio', verbose_name='Фотография')
    photodesc = models.CharField(max_length=100, blank=True, null=True, verbose_name='Описание фото')
