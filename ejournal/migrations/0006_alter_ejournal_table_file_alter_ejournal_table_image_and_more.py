# Generated by Django 4.1.7 on 2023-09-19 16:06

from django.db import migrations, models
import ejournal.models


class Migration(migrations.Migration):
    dependencies = [
        ("ejournal", "0005_historicalsubscription_table_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ejournal_table",
            name="file",
            field=models.FileField(
                upload_to="ejournal_docs/files/",
                validators=[ejournal.models.validate_pdf_file],
            ),
        ),
        migrations.AlterField(
            model_name="ejournal_table",
            name="image",
            field=models.ImageField(
                upload_to="ejournal_docs/cover_images/",
                validators=[ejournal.models.validate_webp_image],
            ),
        ),
        migrations.AlterField(
            model_name="ejournal_table",
            name="name",
            field=models.CharField(
                max_length=1000, validators=[ejournal.models.validate_small_letters]
            ),
        ),
        migrations.AlterField(
            model_name="historicalejournal_table",
            name="file",
            field=models.TextField(
                max_length=100, validators=[ejournal.models.validate_pdf_file]
            ),
        ),
        migrations.AlterField(
            model_name="historicalejournal_table",
            name="image",
            field=models.TextField(
                max_length=100, validators=[ejournal.models.validate_webp_image]
            ),
        ),
        migrations.AlterField(
            model_name="historicalejournal_table",
            name="name",
            field=models.CharField(
                max_length=1000, validators=[ejournal.models.validate_small_letters]
            ),
        ),
    ]