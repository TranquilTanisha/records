# Generated by Django 4.1.3 on 2023-03-17 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0017_alter_row_options_alter_table_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='value',
            field=models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], default='Public', max_length=200),
        ),
    ]