# Generated by Django 4.0.3 on 2022-03-18 17:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Neighbor',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('location', models.TextField()),
                ('occupation', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
