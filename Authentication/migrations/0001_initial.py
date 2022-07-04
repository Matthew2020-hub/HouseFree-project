# Generated by Django 3.2.10 on 2022-07-04 19:10

import Authentication.models
import Authentication.validators
from django.db import migrations, models
import django.utils.timezone
import django_countries.fields
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerifyCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8, verbose_name=' Verification Code ')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name=' Generation time ')),
            ],
            options={
                'ordering': ['-add_time'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('entry', models.CharField(choices=[('Tenant', 'Tenant'), ('Agent', 'Agent')], max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='Full Name')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('agent_location', models.CharField(blank=True, max_length=150, null=True)),
                ('balance', models.FloatField(default=0, validators=[Authentication.validators.minimum_amount])),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_verify', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', Authentication.models.CustomUserManager()),
            ],
        ),
    ]
