# Generated by Django 3.2.20 on 2023-07-10 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='content',
            new_name='interests',
        ),
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.TextField(blank=True),
        ),
    ]
