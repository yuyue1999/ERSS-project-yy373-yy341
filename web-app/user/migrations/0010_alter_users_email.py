# Generated by Django 4.2 on 2023-04-29 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_packages_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
