# Generated by Django 3.0.8 on 2022-02-01 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0002_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
