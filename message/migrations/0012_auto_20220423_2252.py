# Generated by Django 3.2.10 on 2022-04-23 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0011_auto_20220423_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='short_id',
            field=models.CharField(default='W6D17TVTI', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_id',
            field=models.CharField(default='IEQPLAM3M', max_length=255, unique=True),
        ),
    ]
