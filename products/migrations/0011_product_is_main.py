# Generated by Django 3.0.3 on 2020-03-03 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20200303_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
