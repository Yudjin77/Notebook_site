# Generated by Django 5.1.6 on 2025-03-30 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("learning_logs", "0014_alter_women_options_alter_women_cat_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="UploadFiles",
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
                ("file", models.FileField(upload_to="uploads_model")),
            ],
        ),
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Категория", "verbose_name_plural": "Категории"},
        ),
        migrations.AlterModelOptions(
            name="women",
            options={
                "ordering": ["time_create"],
                "verbose_name": "Известные люди",
                "verbose_name_plural": "Известные люди",
            },
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(
                db_index=True, max_length=100, verbose_name="Категория"
            ),
        ),
    ]
