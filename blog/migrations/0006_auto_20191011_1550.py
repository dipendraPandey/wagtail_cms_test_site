# Generated by Django 2.2.6 on 2019-10-11 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogdetailpage_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogdetailpage',
            old_name='blog_image',
            new_name='banner_image',
        ),
    ]
