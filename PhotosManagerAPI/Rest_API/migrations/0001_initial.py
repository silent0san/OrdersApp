# Generated by Django 4.0.3 on 2022-10-28 08:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('title', models.CharField(max_length=200)),
                ('albumId', models.PositiveIntegerField()),
                ('width', models.PositiveIntegerField()),
                ('height', models.PositiveIntegerField()),
                ('dominant_color', models.CharField(max_length=6)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
    ]