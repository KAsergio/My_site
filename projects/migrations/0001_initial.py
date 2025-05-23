# Generated by Django 5.0 on 2025-04-09 00:40

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("title", models.CharField(max_length=150)),
                ("description", models.TextField()),
                ("content", models.TextField()),
                ("slug", models.SlugField(max_length=100, unique=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now=True)),
                (
                    "image",
                    models.ImageField(
                        default="default_project.jpg", upload_to="projects/"
                    ),
                ),
                ("category", models.CharField(max_length=100)),
                ("github_link", models.URLField(blank=True, null=True)),
                ("live_link", models.URLField(blank=True, null=True)),
                ("technologies", models.CharField(max_length=255)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("in_progress", "En cours"),
                            ("completed", "Terminé"),
                            ("on_hold", "En attente"),
                        ],
                        default="completed",
                        max_length=50,
                    ),
                ),
                ("featured", models.BooleanField(default=False)),
            ],
            options={
                "ordering": ["-date_created"],
            },
        ),
    ]
