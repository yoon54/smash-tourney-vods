# Generated by Django 2.2 on 2020-02-26 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smash_app', '0004_auto_20200225_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='image',
            field=models.ImageField(upload_to='gallery/'),
        ),
    ]
