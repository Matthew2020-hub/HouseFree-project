# Generated by Django 3.2.10 on 2022-06-29 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0014_auto_20220628_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='short_id',
            field=models.CharField(default='A4023TSM0', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_id',
            field=models.CharField(default='VLZ8BLSG2', max_length=255, unique=True),
        ),
    ]
