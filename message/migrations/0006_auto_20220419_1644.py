# Generated by Django 3.2.10 on 2022-04-19 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0005_auto_20220419_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='short_id',
            field=models.CharField(default='DZP5676VE', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_id',
            field=models.CharField(default='0R73K2EF9', max_length=255, unique=True),
        ),
    ]
