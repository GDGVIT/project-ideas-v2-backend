# Generated by Django 2.2 on 2020-02-03 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200203_1736'),
        ('adminApp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
    ]