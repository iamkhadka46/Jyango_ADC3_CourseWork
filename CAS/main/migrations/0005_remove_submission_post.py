# Generated by Django 2.2.7 on 2020-02-06 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200206_2306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='post',
        ),
    ]
