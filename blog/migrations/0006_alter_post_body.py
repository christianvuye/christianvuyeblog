# Generated by Django 5.2.3 on 2025-06-21 02:13

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0005_post_page_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="body",
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name="Text"),
        ),
    ]
