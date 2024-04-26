# Generated by Django 4.1.3 on 2024-04-21 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("movies", "0009_alter_movie_id"),
        ("cinema", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Showtime_events",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("startdate", models.DateTimeField()),
                ("enddate", models.DateTimeField()),
                ("price", models.IntegerField()),
                ("stock", models.IntegerField()),
                (
                    "cinema",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cinema.cinema"
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="movies.movie"
                    ),
                ),
            ],
        ),
    ]