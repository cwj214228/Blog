# Generated by Django 2.0 on 2019-05-06 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('write_basicinformation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicinformation',
            name='head_image',
            field=models.URLField(null=True),
        ),
    ]