# Generated by Django 2.0.2 on 2018-12-20 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
