# Generated by Django 3.0.8 on 2022-03-28 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0041_auto_20220328_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raiseticket',
            name='Type',
            field=models.CharField(choices=[('Query', 'Query'), ('Suggestion', 'Suggestion'), ('Complaint', 'Complaint')], default=None, max_length=50, null=True),
        ),
    ]
