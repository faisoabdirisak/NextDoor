# Generated by Django 4.0.3 on 2022-03-18 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myneighbor', '0003_rename_posts_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbor',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
