# Generated by Django 4.2.2 on 2023-06-26 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_emailname_homeapply'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.ImageField(upload_to='')),
                ('products', models.ImageField(upload_to='')),
                ('blogs', models.ImageField(upload_to='')),
                ('contact', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RenameField(
            model_name='emailname',
            old_name='email',
            new_name='subscription_email',
        ),
    ]
