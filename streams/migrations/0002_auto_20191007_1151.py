# Generated by Django 2.2.6 on 2019-10-07 06:21

from django.db import migrations
import streams.Blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('streams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.core.fields.StreamField([('title_and_text', streams.Blocks.TitleAndTextBlock())], blank=True, null=True),
        ),
    ]
