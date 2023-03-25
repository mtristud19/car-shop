# Generated by Django 4.1.6 on 2023-03-25 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_car_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'brand',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='car',
            name='banrd',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='car.brand'),
        ),
    ]