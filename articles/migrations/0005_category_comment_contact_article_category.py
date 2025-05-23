# Generated by Django 5.0.2 on 2025-05-07 10:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0004_article_views_count"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="comment",
            name="contact",
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name="article",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="articles",
                to="articles.category",
            ),
        ),
    ]
