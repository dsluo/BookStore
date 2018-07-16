# Generated by Django 2.0.6 on 2018-07-16 00:53

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20180715_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='item_picture',
            field=models.ImageField(blank=True, default='books/images/default_book.png', null=True, upload_to=books.models.upload_location),
        ),
    ]