# Generated by Django 4.2.13 on 2024-07-09 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangalib', '0002_alter_author_options_alter_book_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
