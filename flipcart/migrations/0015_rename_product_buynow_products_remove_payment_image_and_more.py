# Generated by Django 4.2.19 on 2025-03-11 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipcart', '0014_payment_buynow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buynow',
            old_name='product',
            new_name='products',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='image',
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
