# Generated by Django 5.0.6 on 2024-05-12 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iha', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='iha',
            name='availability',
            field=models.BooleanField(default=True),
        ),
    ]
