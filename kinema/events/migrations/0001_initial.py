# Generated by Django 4.1.3 on 2024-03-20 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="event",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("theme", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("sponsors", models.CharField(max_length=100)),
                ("countries", models.CharField(max_length=100)),
                ("Description", models.TextField()),
                ("Poster", models.URLField(blank=True, null=True)),
            ],
        ),
    ]