# Generated by Django 4.2.6 on 2024-05-19 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTracker', '0009_delete_weekday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sites',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
