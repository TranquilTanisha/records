# Generated by Django 4.1.3 on 2023-03-17 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0024_rename_row_suggestion_rows'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suggestion',
            name='rows',
        ),
        migrations.AddField(
            model_name='suggestion',
            name='rows',
            field=models.ManyToManyField(blank=True, null=True, to='tables.row'),
        ),
    ]
