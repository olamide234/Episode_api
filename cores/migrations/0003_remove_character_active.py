# Generated by Django 3.1.7 on 2021-05-24 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cores', '0002_auto_20210524_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='active',
        ),
    ]