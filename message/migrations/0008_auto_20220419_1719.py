# Generated by Django 3.2.10 on 2022-04-19 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0007_auto_20220419_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='short_id',
            field=models.CharField(default='XRGKQ6B17', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_id',
            field=models.CharField(default='UQM3QYMEM', max_length=255, unique=True),
        ),
    ]
