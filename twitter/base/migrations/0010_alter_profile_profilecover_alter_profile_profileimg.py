# Generated by Django 4.1.7 on 2023-02-25 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_post_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profilecover',
            field=models.ImageField(blank=True, null=True, upload_to='profile_covers'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images'),
        ),
    ]
