# Generated by Django 4.2.1 on 2023-06-07 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("_UsersAPP", "0001_initial"),
        ("_ToursAPP", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tour",
            name="historian",
            field=models.ManyToManyField(
                blank=True, related_name="tour", to="_UsersAPP.historian"
            ),
        ),
        migrations.AddField(
            model_name="tour",
            name="storyteller",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="tour",
                to="_UsersAPP.storyteller",
            ),
        ),
        migrations.AddField(
            model_name="substop",
            name="stop",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sub_stop",
                to="_ToursAPP.stop",
            ),
        ),
        migrations.AddField(
            model_name="stop",
            name="tour",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="stops",
                to="_ToursAPP.tour",
            ),
        ),
    ]