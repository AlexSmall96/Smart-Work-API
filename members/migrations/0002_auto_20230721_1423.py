# Generated by Django 3.2.20 on 2023-07-21 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={},
        ),
        migrations.RemoveField(
            model_name='member',
            name='created_at',
        ),
    ]
