# Generated by Django 4.0.5 on 2022-07-31 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_imagee_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='images/default.png', upload_to='images/%Y/%m/%d/'),
        ),
    ]
