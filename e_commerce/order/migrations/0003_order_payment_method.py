# Generated by Django 4.0.4 on 2022-04-26 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_cart_color_cart_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Cash on Delivery', 'Cash on Delivery'), ('PayPal', 'PayPal'), ('SSLcommerz', 'SSLcommerz')], default='Cash on Delivery', max_length=30),
        ),
    ]
