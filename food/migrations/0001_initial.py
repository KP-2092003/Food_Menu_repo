# Generated by Django 5.1.6 on 2025-03-03 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_name', models.CharField(max_length=200)),
                ('Item_desc', models.CharField(max_length=100)),
                ('Item_price', models.IntegerField()),
            ],
        ),
    ]
