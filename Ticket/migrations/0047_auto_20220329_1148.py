# Generated by Django 3.0.8 on 2022-03-29 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0046_auto_20220329_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raiseticket',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]