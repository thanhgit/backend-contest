# Generated by Django 2.2.4 on 2019-08-26 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logger',
            name='file_size',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
