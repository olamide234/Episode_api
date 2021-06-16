# Generated by Django 3.1.7 on 2021-06-09 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cores', '0006_auto_20210609_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='location',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='character_id', to='cores.location'),
        ),
    ]