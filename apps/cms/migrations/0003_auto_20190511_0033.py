# Generated by Django 2.0 on 2019-05-10 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20190511_0033'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'ordering': ['-priority']},
        ),
    ]
