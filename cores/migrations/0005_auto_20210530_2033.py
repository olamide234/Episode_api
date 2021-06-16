# Generated by Django 3.1.7 on 2021-05-30 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cores', '0004_auto_20210529_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='episodes',
            field=models.ManyToManyField(blank=True, to='cores.Episode'),
        ),
        migrations.RemoveField(
            model_name='episode',
            name='characters',
        ),
        migrations.AddField(
            model_name='episode',
            name='characters',
            field=models.ManyToManyField(to='cores.Character'),
        ),
    ]
