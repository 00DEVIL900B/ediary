# Generated by Django 4.2.9 on 2024-01-19 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
