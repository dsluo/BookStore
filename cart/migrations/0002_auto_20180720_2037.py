# Generated by Django 2.0.6 on 2018-07-21 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
        ('members', '0001_initial'),
        ('books', '0002_book_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address_used',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='address_used', to='members.Address'),
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(blank=True, to='cart.CartItem'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book'),
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, to='cart.CartItem'),
        ),
    ]
