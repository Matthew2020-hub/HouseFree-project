# Generated by Django 3.2.10 on 2022-06-29 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0022_auto_20220629_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='short_id',
            field=models.CharField(default='TCNXE2Q37', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_id',
            field=models.CharField(default='LPF6AAWGP', max_length=255, unique=True),
        ),
    ]
