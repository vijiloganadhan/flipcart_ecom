# Generated by Django 4.2.19 on 2025-03-10 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipcart', '0012_delete_ratings'),
    ]

    operations = [
        migrations.CreateModel(
            name='I',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/')),
            ],
        ),
    ]
