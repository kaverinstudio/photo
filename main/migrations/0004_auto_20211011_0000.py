# Generated by Django 3.2 on 2021-10-10 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='photo_tumb',
            field=models.ImageField(default=1, upload_to='portfolio/thumbnails', verbose_name='Иконка'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='photo',
            field=models.ImageField(upload_to='portfolio', verbose_name='Фотография'),
        ),
    ]
