# Generated by Django 3.0.8 on 2022-03-28 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0044_auto_20220328_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raiseticket',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
