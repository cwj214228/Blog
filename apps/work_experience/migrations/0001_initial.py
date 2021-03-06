# Generated by Django 2.0 on 2019-05-06 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(max_length=20, null=True)),
                ('end_time', models.CharField(max_length=20, null=True)),
                ('position', models.CharField(max_length=50, null=True)),
                ('work_one', models.CharField(max_length=200, null=True)),
                ('work_two', models.CharField(max_length=200, null=True)),
                ('work_three', models.CharField(max_length=200, null=True)),
                ('work_four', models.CharField(max_length=200, null=True)),
                ('work_five', models.CharField(max_length=200, null=True)),
                ('work_skill_one', models.CharField(max_length=200, null=True)),
                ('work_skill_two', models.CharField(max_length=200, null=True)),
                ('work_skill_three', models.CharField(max_length=200, null=True)),
                ('work_skill_four', models.CharField(max_length=200, null=True)),
                ('work_skill_five', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
