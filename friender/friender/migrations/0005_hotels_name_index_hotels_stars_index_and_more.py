# Generated by Django 5.0.6 on 2024-05-20 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friender', '0004_user_remove_hotel_owner_hotels_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='hotels',
            index=models.Index(fields=['name'], name='name_index'),
        ),
        migrations.AddIndex(
            model_name='hotels',
            index=models.Index(fields=['stars'], name='stars_index'),
        ),
        migrations.AddIndex(
            model_name='hotels',
            index=models.Index(fields=['city'], name='city_index'),
        ),
        migrations.AddIndex(
            model_name='hotels',
            index=models.Index(fields=['owners'], name='owners_index'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['first_name'], name='first_name_index'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['last_name'], name='last_name_index'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['age'], name='age_index'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['sex'], name='sex_index'),
        ),
    ]
