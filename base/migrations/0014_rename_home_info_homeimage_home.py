# Generated by Django 4.2.2 on 2023-06-26 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_rename_project_count_funfact_count_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homeimage',
            old_name='home_info',
            new_name='home',
        ),
    ]