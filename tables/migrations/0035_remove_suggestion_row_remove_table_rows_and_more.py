# Generated by Django 4.1.3 on 2023-03-17 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0034_rename_row_table_rows'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suggestion',
            name='row',
        ),
        migrations.RemoveField(
            model_name='table',
            name='rows',
        ),
        migrations.AddField(
            model_name='row',
            name='table_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.table'),
        ),
    ]
