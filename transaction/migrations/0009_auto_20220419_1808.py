# Generated by Django 3.2.10 on 2022-04-19 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0008_auto_20220419_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymenthistory',
            name='short_id',
            field=models.CharField(default='FXOH5OY14', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='room_id',
            field=models.CharField(default='1L8K8LS91', max_length=255, unique=True),
        ),
    ]