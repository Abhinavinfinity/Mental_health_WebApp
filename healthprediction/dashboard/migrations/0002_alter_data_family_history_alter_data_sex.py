# Generated by Django 4.1.4 on 2022-12-25 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='family_history',
            field=models.PositiveIntegerField(choices=[(0, 'No'), (1, 'Yes')], null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='sex',
            field=models.PositiveIntegerField(choices=[(0, 'Female'), (1, 'Male')], null=True),
        ),
    ]
