# Generated by Django 5.2 on 2025-04-11 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='logo',
            field=models.ImageField(default='no_headshot.png', upload_to='customers'),
        ),
    ]
