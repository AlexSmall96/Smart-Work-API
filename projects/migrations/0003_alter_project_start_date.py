# Generated by Django 3.2.20 on 2023-07-11 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
