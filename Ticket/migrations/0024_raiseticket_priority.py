# Generated by Django 3.0.8 on 2022-03-09 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0023_auto_20220309_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='raiseticket',
            name='priority',
            field=models.CharField(choices=[('High', 'High'), ('Low', 'Low'), ('Medium', 'Medium')], default='Medium', max_length=50),
        ),
    ]
