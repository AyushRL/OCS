# Generated by Django 5.0 on 2024-03-04 16:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="myuser",
            name="is_admin",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
