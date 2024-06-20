# Generated by Django 5.0.6 on 2024-06-20 17:15

import ckeditor.fields
import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255, null=True, unique=True)),
                ('description', ckeditor.fields.RichTextField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WeddingHall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('price_morning', models.CharField(max_length=50, null=True)),
                ('price_afternoon', models.CharField(max_length=50, null=True)),
                ('price_evening', models.CharField(max_length=50, null=True)),
                ('price_weekend', models.CharField(max_length=50, null=True)),
                ('image', models.ImageField(upload_to='anres/%Y/%m')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WeddingMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('avatar', models.ImageField(upload_to='anres/%Y/%m')),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('staff', 'Staff'), ('customer', 'Customer')], max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BanquetRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('capacity', models.IntegerField(null=True)),
                ('area', models.IntegerField(null=True)),
                ('kind_of_table', models.CharField(max_length=50)),
                ('table', models.IntegerField(null=True)),
                ('stage', models.IntegerField(null=True)),
                ('room_shape', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='anres/%Y/%m')),
                ('wedding_hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anwedding.weddinghall')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FoodMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='anres/%Y/%m')),
                ('food_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anwedding.fooditem')),
                ('wedding_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anwedding.weddingmenu')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WeddingService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
                ('homepage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anwedding.homepage')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='weddingmenu',
            name='wedding_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anwedding.weddingservice'),
        ),
        migrations.AddField(
            model_name='weddinghall',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anwedding.weddingservice'),
        ),
        migrations.CreateModel(
            name='WeddingBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('total_price', models.CharField(max_length=50, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anwedding.weddinghall')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anwedding.weddingmenu')),
                ('service', models.ManyToManyField(to='anwedding.weddingservice')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='fooditem',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anwedding.weddingservice'),
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wedding_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anwedding.weddingservice')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
