# Generated by Django 4.1.4 on 2022-12-18 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Penerbangan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("asal", models.CharField(max_length=64)),
                ("tujuan", models.CharField(max_length=64)),
                ("durasi", models.IntegerField()),
            ],
        ),
    ]
