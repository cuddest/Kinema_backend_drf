# Generated by Django 4.1.3 on 2024-04-02 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("movies", "0009_alter_movie_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="item",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("description", models.TextField()),
                ("name", models.CharField(max_length=100)),
                ("price", models.IntegerField()),
                ("points_price", models.IntegerField()),
                ("stock", models.IntegerField()),
                ("imgurl", models.URLField(blank=True, null=True)),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="movies.movie"
                    ),
                ),
            ],
        ),
    ]
