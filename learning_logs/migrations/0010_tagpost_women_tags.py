# Generated by Django 5.1.6 on 2025-03-24 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("learning_logs", "0009_alter_category_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="TagPost",
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
                ("tag", models.CharField(db_index=True, max_length=100)),
                ("slug", models.SlugField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name="women",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="tags", to="learning_logs.tagpost"
            ),
        ),
    ]
