# Generated by Django 3.0 on 2021-05-22 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0013_auto_20210522_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='file_upload',
            field=models.FileField(blank=True, null=True, upload_to='media/files/'),
        ),
    ]
