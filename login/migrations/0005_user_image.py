# Generated by Django 4.1 on 2022-08-20 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_user_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
