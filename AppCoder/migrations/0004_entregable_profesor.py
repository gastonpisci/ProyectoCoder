# Generated by Django 5.0.1 on 2024-01-21 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppCoder", "0003_estudiante_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Entregable",
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
                ("nombre", models.CharField(max_length=50)),
                ("fechaDeEntrega", models.DateField()),
                ("entregado", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Profesor",
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
                ("nombre", models.CharField(max_length=50)),
                ("apellido", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254, null=True)),
                ("profesion", models.CharField(max_length=50)),
            ],
        ),
    ]
