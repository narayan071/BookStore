# Generated by Django 4.2.3 on 2023-07-15 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book',
        ),
    ]
