# Generated by Django 4.2.2 on 2023-10-17 15:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="is_valid",
            field=models.BooleanField(default=False),
        ),
    ]
