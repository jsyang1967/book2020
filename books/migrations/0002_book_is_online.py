# Generated by Django 3.0.3 on 2020-02-03 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_online',
            field=models.NullBooleanField(default=True),
        ),
    ]