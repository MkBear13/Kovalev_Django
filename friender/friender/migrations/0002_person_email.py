# Generated by Django 5.0.4 on 2024-05-08 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friender', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
