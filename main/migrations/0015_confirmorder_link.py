# Generated by Django 4.0 on 2022-01-20 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_confirmorder_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmorder',
            name='link',
            field=models.FilePathField(allow_folders=True, blank=True, null=True),
        ),
    ]
