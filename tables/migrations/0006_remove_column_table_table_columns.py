# Generated by Django 4.1.3 on 2023-01-27 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0005_table_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='column',
            name='table',
        ),
        migrations.AddField(
            model_name='table',
            name='columns',
            field=models.ManyToManyField(blank=True, to='tables.column'),
        ),
    ]