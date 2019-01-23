# Generated by Django 2.1.5 on 2019-01-23 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodname', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('presence', models.BooleanField(choices=[(True, 'In Stock'), (False, 'Not available')])),
                ('description', models.TextField(blank=True)),
                ('price', models.FloatField()),
                ('os_name', models.CharField(max_length=50)),
                ('diagonal', models.FloatField()),
                ('ram', models.IntegerField()),
                ('memory', models.IntegerField()),
                ('vcard', models.CharField(max_length=100)),
                ('relevance', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(to='app.Category')),
            ],
            options={
                'ordering': ['-relevance'],
            },
        ),
    ]
