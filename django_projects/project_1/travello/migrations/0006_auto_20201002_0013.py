# Generated by Django 3.1.1 on 2020-10-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0005_auto_20201002_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='img',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
