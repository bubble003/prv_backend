# Generated by Django 4.1.7 on 2023-08-19 12:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("analytics", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="historicaltest_table",
            name="history_user",
        ),
        migrations.DeleteModel(
            name="test_table",
        ),
        migrations.DeleteModel(
            name="Historicaltest_table",
        ),
    ]