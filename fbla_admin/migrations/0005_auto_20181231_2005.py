# Generated by Django 2.1.4 on 2018-12-31 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbla_admin', '0004_auto_20181231_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, upload_to='book_images/', verbose_name='Cover Image'),
        ),
    ]
