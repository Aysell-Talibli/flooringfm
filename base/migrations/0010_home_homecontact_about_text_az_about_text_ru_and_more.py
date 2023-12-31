# Generated by Django 4.2.2 on 2023-06-25 19:29

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_socialmedia_link_alter_socialmedia_app'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='HomeContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='about',
            name='text_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='text_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='slug_az',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='slug_ru',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='text_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='text_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_az',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_az',
            field=models.CharField(default='Others', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(default='Others', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='main',
            name='footer_logo',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='main',
            name='footer_text',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='main',
            name='footer_text_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='main',
            name='footer_text_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='main',
            name='header_logo',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='main',
            name='home_logo',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='name_az',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='name_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='portfoliocategory',
            name='name_az',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='portfoliocategory',
            name='name_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_az',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Mehsul haqqinda etrafli melumat'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Mehsul haqqinda etrafli melumat'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_az',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug_az',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug_ru',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.CreateModel(
            name='HomeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('home_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='base.home')),
            ],
        ),
    ]
