# Generated by Django 4.1.4 on 2022-12-25 10:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_data_family_history_alter_data_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='age',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(15), django.core.validators.MaxValueValidator(60)]),
        ),
    ]
