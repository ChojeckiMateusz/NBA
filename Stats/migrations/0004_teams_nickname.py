# Generated by Django 3.1.4 on 2021-01-29 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stats', '0003_auto_20210129_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='nickname',
            field=models.CharField(default='', max_length=15),
        ),
    ]
