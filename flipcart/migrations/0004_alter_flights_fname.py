# Generated by Django 4.2.19 on 2025-03-09 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flipcart', '0003_todayflights_alter_flights_fname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flights',
            name='fname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='flipcart.todayflights'),
        ),
    ]
