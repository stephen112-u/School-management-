# Generated by Django 3.0 on 2021-05-22 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0012_notice_file_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='file_upload',
            field=models.FileField(blank=True, null=True, upload_to='pdfs/'),
        ),
    ]
