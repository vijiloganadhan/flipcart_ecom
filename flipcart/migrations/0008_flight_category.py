# Generated by Django 4.2.19 on 2025-03-09 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipcart', '0007_remove_todayflights_flightscat_delete_flightcategory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='image/')),
            ],
        ),
    ]
