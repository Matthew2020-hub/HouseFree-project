# Generated by Django 3.2.10 on 2022-06-14 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_auto_20220614_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='short_id',
            field=models.CharField(default='LUC820E81', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_id',
            field=models.CharField(default='29QA6K5S8', max_length=255, unique=True),
        ),
    ]
