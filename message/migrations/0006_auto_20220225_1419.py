# Generated by Django 3.2.10 on 2022-02-25 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0005_auto_20220225_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='short_id',
            field=models.CharField(default='85XISE3SV', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_id',
            field=models.CharField(default='DBF2J0DLC', max_length=255, unique=True),
        ),
    ]