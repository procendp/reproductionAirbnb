# Generated by Django 5.1.3 on 2024-11-25 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(blank=True, default='', max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Amenities',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=180)),
                ('country', models.CharField(default='South Korea', max_length=50)),
                ('city', models.CharField(default='Seoul', max_length=80)),
                ('price', models.PositiveIntegerField()),
                ('rooms', models.PositiveIntegerField()),
                ('toilets', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=250)),
                ('pet_friendly', models.BooleanField(default=True)),
                ('kind', models.CharField(choices=[('entire_place', 'Entire Place'), ('private_room', 'Private Room'), ('shared_room', 'Shared Room')], max_length=20)),
                ('amenities', models.ManyToManyField(to='rooms.amenity')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
