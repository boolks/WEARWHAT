# Generated by Django 3.0.5 on 2020-08-24 09:29

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('brand', models.TextField(blank=True, null=True)),
                ('season', models.TextField(blank=True, null=True)),
                ('gender', models.TextField(blank=True, null=True)),
                ('color', models.TextField(blank=True, null=True)),
                ('category', models.TextField(blank=True, null=True)),
                ('image', models.TextField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'clothes005',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Top',
            fields=[
                ('id', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('brand', models.TextField(blank=True, null=True)),
                ('season', models.TextField(blank=True, null=True)),
                ('gender', models.TextField(blank=True, null=True)),
                ('color', models.TextField(blank=True, null=True)),
                ('category', models.TextField(blank=True, null=True)),
                ('image', models.TextField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'clothes001',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Under',
            fields=[
                ('id', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('brand', models.TextField(blank=True, null=True)),
                ('season', models.TextField(blank=True, null=True)),
                ('gender', models.TextField(blank=True, null=True)),
                ('color', models.TextField(blank=True, null=True)),
                ('category', models.TextField(blank=True, null=True)),
                ('image', models.TextField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'clothes003',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=10, null=True)),
                ('gender', models.CharField(choices=[('M', '남성'), ('W', '여성')], max_length=1, verbose_name='성별')),
                ('fav_style', models.CharField(choices=[('FORMAL', '포멀'), ('CASUAL', '캐주얼')], max_length=6, verbose_name='선호 스타일')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('like_shoes', models.ManyToManyField(blank=True, related_name='liked_shoes', to='wearwhat.Shoes')),
                ('like_under', models.ManyToManyField(blank=True, related_name='liked_under', to='wearwhat.Under')),
                ('liked_top', models.ManyToManyField(blank=True, related_name='liked_top', to='wearwhat.Top')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
