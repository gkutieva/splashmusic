# Generated by Django 3.1.4 on 2021-01-05 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20210105_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='date',
            field=models.DateField(),
        ),
    ]
