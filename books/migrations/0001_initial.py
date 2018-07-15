# Generated by Django 2.0.7 on 2018-07-14 18:51

import books.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_picture', models.ImageField(blank=True, null=True, upload_to=books.models.upload_location)),
                ('name', models.CharField(max_length=120)),
                ('isbn', models.CharField(max_length=30, unique=True)),
                ('publisher', models.CharField(max_length=60)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('publish_date', models.DateField()),
                ('count_in_stock', models.IntegerField(blank=True, default=1)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='books.Book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='subjects',
            field=models.ManyToManyField(to='books.Genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vendors.Vendor'),
        ),
    ]
