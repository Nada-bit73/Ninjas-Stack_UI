# Generated by Django 2.2.4 on 2022-07-08 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0005_delete_videos'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(related_name='blogpost_like', to='app_one.User'),
        ),
    ]
