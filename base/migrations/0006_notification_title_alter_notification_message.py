# Generated by Django 4.1.7 on 2024-07-26 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='title',
            field=models.CharField(default='No Title', max_length=100),
        ),
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.TextField(default='No Message'),
        ),
    ]
