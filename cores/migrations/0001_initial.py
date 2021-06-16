# Generated by Django 3.1.7 on 2021-05-19 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=64)),
                ('lastName', models.CharField(max_length=64)),
                ('status', models.CharField(choices=[('AC', 'Active'), ('DD', 'Dead'), ('UK', 'Unknown')], max_length=2)),
                ('stateOfOrigin', models.CharField(blank=True, max_length=64)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(max_length=249)),
                ('ipAddressLocation', models.GenericIPAddressField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('released_date', models.DateTimeField(auto_now_add=True)),
                ('episodeCode', models.CharField(max_length=64)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('characters', models.ManyToManyField(to='cores.Character')),
                ('episodeComments', models.ManyToManyField(to='cores.Comment')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='episodes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cores.episode'),
        ),
        migrations.AddField(
            model_name='character',
            name='location',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cores.location'),
        ),
    ]
