# Generated by Django 4.0 on 2022-01-20 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_confirmorder_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmorder',
            name='session_key',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
