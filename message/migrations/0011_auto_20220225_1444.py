# Generated by Django 3.2.10 on 2022-02-25 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0010_auto_20220225_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='short_id',
            field=models.CharField(default='DE8AX8C1H', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_id',
            field=models.CharField(default='Y2EKYVDHC', max_length=255, unique=True),
        ),
    ]