# Generated by Django 4.1.2 on 2022-11-11 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cleaning", "0003_alter_review_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="guest",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=models.IntegerField(max_length=10),
        ),
    ]
