# Generated by Django 4.1.7 on 2023-03-20 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_landinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landinfo',
            name='area',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='landinfo',
            name='contact',
            field=models.CharField(max_length=12, null=True),
        ),
    ]