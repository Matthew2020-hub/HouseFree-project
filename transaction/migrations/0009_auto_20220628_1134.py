# Generated by Django 3.2.10 on 2022-06-28 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0008_auto_20220628_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymenthistory',
            name='short_id',
            field=models.CharField(default='14HWYCQIA', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='room_id',
            field=models.CharField(default='1AEQ9IVQN', max_length=255, unique=True),
        ),
    ]
