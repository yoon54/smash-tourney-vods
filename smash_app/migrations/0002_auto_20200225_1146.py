# Generated by Django 2.2 on 2020-02-25 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smash_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='image',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]