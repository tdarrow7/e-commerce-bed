# Generated by Django 4.2.13 on 2024-06-14 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0008_brand_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='dateAdded',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
