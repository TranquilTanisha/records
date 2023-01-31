# Generated by Django 4.1.5 on 2023-01-26 16:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('title', models.TextField()),
                ('col1', models.TextField(blank=True, null=True)),
                ('col2', models.TextField(blank=True, null=True)),
                ('col3', models.TextField(blank=True, null=True)),
                ('col4', models.TextField(blank=True, null=True)),
                ('col5', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('total', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
