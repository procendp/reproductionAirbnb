# Generated by Django 5.1.3 on 2024-11-28 16:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0004_alter_experience_category_alter_experience_host_and_more'),
        ('reviews', '0002_rename_payroad_review_payload'),
        ('rooms', '0004_alter_room_amenities_alter_room_category_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='experience',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='experiences.experience'),
        ),
        migrations.AlterField(
            model_name='review',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='rooms.room'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
