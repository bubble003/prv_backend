# Generated by Django 4.1.7 on 2023-04-04 19:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("footer", "0004_alter_footer_table_timestamp"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="footer_table",
            options={"ordering": ["-created_at"]},
        ),
        migrations.RemoveField(
            model_name="footer_table",
            name="timestamp",
        ),
        migrations.AddField(
            model_name="footer_table",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 4, 19, 59, 9, 431849, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AddField(
            model_name="footer_table",
            name="modified_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 4, 19, 59, 9, 431862, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
