# Generated by Django 4.0.4 on 2022-04-22 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='head_image',
            field=models.ImageField(blank=True, upload_to='landing/images/%Y/%m/%d/%H/'),
        ),
    ]
