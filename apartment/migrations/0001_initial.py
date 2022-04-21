# Generated by Django 3.2.10 on 2022-02-24 11:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('apartment_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('aparment_title', models.CharField(max_length=40, null=True, verbose_name='Apartment Title')),
                ('category', models.CharField(max_length=50, null=True)),
                ('image', models.ImageField(blank=True, upload_to='apartment/')),
                ('videofile', models.FileField(blank=True, null=True, upload_to='video/')),
                ('price', models.CharField(max_length=50, null=True)),
                ('location', models.CharField(max_length=30, null=True)),
                ('agent', models.CharField(max_length=30, null=True)),
                ('descriptions', models.CharField(max_length=250, null=True)),
                ('feautures', models.CharField(max_length=250, null=True)),
                ('location_info', models.CharField(max_length=250, null=True)),
                ('reviews', models.CharField(max_length=250, null=True)),
                ('is_available', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['category'],
            },
        ),
    ]
