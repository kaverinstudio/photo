# Generated by Django 3.2 on 2021-10-02 07:20

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(blank=True, max_length=500, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя заказчика')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефон заказчика')),
                ('delivery', models.CharField(blank=True, max_length=50, null=True, verbose_name='Способ доставки')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Адрес доставки')),
                ('comment', models.CharField(blank=True, max_length=500, null=True, verbose_name='Комментарии к заказу')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('link', models.FilePathField(allow_folders=True, blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Сформированный заказ',
                'verbose_name_plural': 'Сформированные заказы',
            },
        ),
        migrations.CreateModel(
            name='MainCardModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='site-images', verbose_name='Изображение')),
                ('description', models.CharField(max_length=150, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Карточка на главной странице',
                'verbose_name_plural': 'Карточки на главной странице',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_session_key', models.CharField(blank=True, max_length=100, null=True)),
                ('order_count', models.PositiveBigIntegerField(blank=True, null=True)),
                ('order_format', models.CharField(blank=True, max_length=10, null=True)),
                ('order_papier', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'Временный заказ',
                'verbose_name_plural': 'Временные заказы',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format', models.CharField(blank=True, choices=[('10x15', '10x15'), ('15x21', '15x21'), ('20x30', '20x30')], default='10x15', max_length=100)),
                ('file', models.ImageField(upload_to=main.models.user_directory_path)),
                ('session_key', models.CharField(blank=True, max_length=100, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('count', models.PositiveBigIntegerField(blank=True, default='1', null=True)),
                ('papier', models.CharField(blank=True, choices=[('Глянцевая', 'Глянцевая'), ('Матовая', 'Матовая')], default='Глянцевая', max_length=20)),
            ],
            options={
                'verbose_name': 'Фотографии заказа',
                'verbose_name_plural': 'Фотографии заказов',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Услуга')),
                ('cost', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Услуга и цена',
                'verbose_name_plural': 'Услуги и цены',
            },
        ),
    ]
