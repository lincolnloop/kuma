# Generated by Django 3.2.7 on 2021-11-01 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notifications", "0002_auto_20211101_1528"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="read",
            field=models.BooleanField(default=False),
        ),
    ]
