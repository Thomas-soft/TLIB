# Generated by Django 4.2.13 on 2024-07-10 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='a',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
