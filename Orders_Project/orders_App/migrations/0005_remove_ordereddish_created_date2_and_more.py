# Generated by Django 4.0.3 on 2024-02-13 16:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders_App', '0004_ordereddish_created_date2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordereddish',
            name='created_date2',
        ),
        migrations.AlterField(
            model_name='ordereddish',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created Date'),
        ),
    ]
