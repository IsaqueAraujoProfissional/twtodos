# Generated by Django 5.1.1 on 2024-09-13 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="deadline",
            field=models.DateTimeField(),
        ),
    ]