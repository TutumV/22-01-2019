# Generated by Django 2.1.5 on 2019-01-23 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190123_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='presence',
            field=models.BooleanField(default=True),
        ),
    ]
