# Generated by Django 4.0.4 on 2022-08-01 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_rename_purchaser_store_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
