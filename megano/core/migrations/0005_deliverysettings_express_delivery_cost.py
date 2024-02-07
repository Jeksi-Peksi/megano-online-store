# Generated by Django 4.2.2 on 2023-12-25 13:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_alter_deliverysettings_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="deliverysettings",
            name="express_delivery_cost",
            field=models.PositiveIntegerField(
                default=500, verbose_name="express_delivery_cost"
            ),
        ),
    ]
