# Generated by Django 3.0.8 on 2022-02-08 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0015_automation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='automation',
            name='is_superuser',
        ),
        migrations.AddField(
            model_name='automation',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
