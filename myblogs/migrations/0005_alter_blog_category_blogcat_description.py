# Generated by Django 5.0.1 on 2024-01-15 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogs', '0004_alter_blog_category_blogcat_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_category',
            name='blogcat_description',
            field=models.CharField(max_length=1000),
        ),
    ]