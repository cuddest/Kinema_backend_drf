# Generated by Django 4.1.3 on 2024-03-17 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0005_rename_production_companies_movie_productioncompanies"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="Cast",
            field=models.CharField(default=list, max_length=100),
        ),
    ]
