# Generated by Django 5.0.1 on 2024-01-19 10:25

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblogs', '0008_blog_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='blog_description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
