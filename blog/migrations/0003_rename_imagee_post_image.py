# Generated by Django 4.0.5 on 2022-07-31 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_imagee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='imagee',
            new_name='image',
        ),
    ]
