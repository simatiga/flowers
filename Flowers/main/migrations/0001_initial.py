# Generated by Django 4.0.3 on 2022-04-28 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='plant_ctgry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('col1', models.TextField()),
                ('col2', models.IntegerField()),
                ('col3', models.FloatField()),
                ('col4', models.TextField()),
            ],
        ),
    ]
