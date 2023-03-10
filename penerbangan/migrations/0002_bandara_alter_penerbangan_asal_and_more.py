# Generated by Django 4.1.4 on 2022-12-18 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("penerbangan", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Bandara",
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
                ("kode", models.CharField(max_length=3)),
                ("kota", models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name="penerbangan",
            name="asal",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="departemen",
                to="penerbangan.bandara",
            ),
        ),
        migrations.AlterField(
            model_name="penerbangan",
            name="tujuan",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="kedatangan",
                to="penerbangan.bandara",
            ),
        ),
    ]
