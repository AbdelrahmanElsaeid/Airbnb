# Generated by Django 4.1.7 on 2023-03-23 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.Generate_code


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserNumbers",
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
                ("number", models.CharField(max_length=20)),
                (
                    "type",
                    models.CharField(
                        choices=[("Primary", "Primary"), ("Secondary", "Secondary")],
                        max_length=12,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_phones",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserAddress",
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
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Home", "Home"),
                            ("Office", "Office"),
                            ("Business", "Business"),
                            ("Academy", "Academy"),
                            ("Other", "Other"),
                        ],
                        max_length=12,
                    ),
                ),
                ("city", models.CharField(max_length=20)),
                ("region", models.CharField(max_length=20)),
                ("street", models.CharField(max_length=20)),
                ("appartment", models.CharField(max_length=20)),
                ("notes", models.CharField(max_length=20)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_address",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
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
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default="default.png",
                        null=True,
                        upload_to="profile",
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        default=utils.Generate_code.generate_code, max_length=8
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
