# Generated by Django 5.0.6 on 2024-05-24 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_Theme',
        ),
    ]
