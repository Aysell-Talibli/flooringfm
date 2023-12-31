# Generated by Django 4.2.2 on 2023-06-22 12:53

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_main_map_portfoliocategory_socialmedia_portfolio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='apply',
            name='phone',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Mehsul haqqinda etrafli melumat'),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='app',
            field=models.CharField(choices=[('insta', 'Instagram')], max_length=100),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.product')),
            ],
        ),
    ]
