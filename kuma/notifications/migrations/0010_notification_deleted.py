# Generated by Django 3.2.10 on 2022-01-27 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notifications", "0009_notificationdata_page_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="deleted",
            field=models.BooleanField(default=False),
        ),
    ]