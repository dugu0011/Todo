# Generated by Django 3.0.8 on 2022-03-29 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0045_auto_20220328_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raiseticket',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
