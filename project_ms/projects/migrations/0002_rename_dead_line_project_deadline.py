# Generated by Django 4.0.2 on 2022-02-12 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='dead_line',
            new_name='deadline',
        ),
    ]
