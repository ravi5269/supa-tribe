# Generated by Django 4.2.2 on 2023-07-24 09:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("users", "0006_remove_user_is_superuser")]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
    ]
