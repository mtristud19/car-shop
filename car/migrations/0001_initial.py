# Generated by Django 4.1.6 on 2023-03-15 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'db_carshop',
                'ordering': ['name'],
            },
        ),
    ]
