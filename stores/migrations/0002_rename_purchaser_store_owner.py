# Generated by Django 4.0.4 on 2022-08-01 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='purchaser',
            new_name='owner',
        ),
    ]