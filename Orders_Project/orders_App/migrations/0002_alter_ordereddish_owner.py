# Generated by Django 4.0.3 on 2024-02-12 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordereddish',
            name='owner',
            field=models.CharField(default='', max_length=150),
        ),
    ]
