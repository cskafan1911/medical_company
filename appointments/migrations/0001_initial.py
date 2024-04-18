# Generated by Django 4.2.7 on 2024-04-18 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Appointment",
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
                ("date", models.DateField(verbose_name="Дата")),
                ("time", models.TimeField(blank=True, null=True, verbose_name="Время")),
                (
                    "status_of_appointment",
                    models.CharField(
                        choices=[
                            ("WAITING", "ожидание приема"),
                            ("COMPLETED", "прием оказан"),
                            ("CANCELLED", "прием отменен"),
                        ],
                        default="WAITING",
                        max_length=20,
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                (
                    "price",
                    models.FloatField(blank=True, null=True, verbose_name="Цена"),
                ),
            ],
            options={
                "verbose_name": "Запись",
                "verbose_name_plural": "Записи",
            },
        ),
        migrations.CreateModel(
            name="Timetable",
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
                    "day_of_visit",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (0, "Monday"),
                            (1, "Tuesday"),
                            (2, "Wednesday"),
                            (3, "Thursday"),
                            (4, "Friday"),
                            (5, "Saturday"),
                            (6, "Sunday"),
                        ],
                        unique=True,
                        verbose_name="День приема",
                    ),
                ),
            ],
            options={
                "verbose_name": "Расписание",
                "verbose_name_plural": "Расписания",
            },
        ),
    ]
